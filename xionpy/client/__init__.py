import json
import math
from dataclasses import dataclass
from typing import Any, Optional, Tuple

import backoff
import certifi
import grpc
from dateutil.parser import isoparse

from xionpy.bank.rest_client import BankRestClient
from xionpy.client.config import NetworkConfig
from xionpy.client.exceptions import InvalidDenominationError, NotFoundError
from xionpy.client.gas import GasStrategy, SimulationGasStrategy
from xionpy.client.messages.bank import msg_send
from xionpy.client.tx import MessageLog, SubmittedTx, Transaction, TxResponse, TxState
from xionpy.client.urls import Protocol, parse_url
from xionpy.client.utils import tx_submit_basic
from xionpy.client.wallet import Wallet
from xionpy.common.rest_client import RestClient
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from xionpy.protos.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest
from xionpy.protos.cosmos.auth.v1beta1.query_pb2_grpc import (
    QueryStub as AuthQueryClient,
)
from xionpy.protos.cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest
from xionpy.protos.cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankGrpcClient
from xionpy.protos.cosmos.params.v1beta1.query_pb2 import QueryParamsRequest
from xionpy.protos.cosmos.params.v1beta1.query_pb2_grpc import (
    QueryStub as ParamsQueryClient,
)
from xionpy.protos.cosmos.tx.v1beta1.service_pb2 import (
    BroadcastMode,
    BroadcastTxRequest,
    SimulateRequest, GetTxRequest,
)
from xionpy.protos.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub as TxGrpcClient
from xionpy.tx.rest_client import TxRestClient

DEFAULT_QUERY_TIMEOUT_SECS = 30
DEFAULT_QUERY_INTERVAL_SECS = 2


@dataclass
class Account:
    """Account."""

    address: Address
    number: int
    sequence: int


class XionClient:

    def __init__(
            self,
            cfg: NetworkConfig,
            query_interval_secs: int = DEFAULT_QUERY_INTERVAL_SECS,
            query_timeout_secs: int = DEFAULT_QUERY_TIMEOUT_SECS,
    ):
        self._query_interval_secs = query_interval_secs
        self._query_timeout_secs = query_timeout_secs
        cfg.validate()
        self.network_config = cfg
        self.gas_strategy: GasStrategy = SimulationGasStrategy(self)

        parsed_url = parse_url(cfg.url)

        if parsed_url.protocol == Protocol.GRPC:
            if parsed_url.secure:
                with open(certifi.where(), "rb") as f:
                    trusted_certs = f.read()
                credentials = grpc.ssl_channel_credentials(
                    root_certificates=trusted_certs
                )
                grpc_client = grpc.secure_channel(parsed_url.host_and_port, credentials)
            else:
                grpc_client = grpc.insecure_channel(parsed_url.host_and_port)

            self.auth = AuthQueryClient(grpc_client)
            self.bank = BankGrpcClient(grpc_client)
            self.params = ParamsQueryClient(grpc_client)
            self.txs = TxGrpcClient(grpc_client)

        else:
            rest_client = RestClient(parsed_url.rest_url)

            self.bank = BankRestClient(rest_client)
            self.txs = TxRestClient(rest_client)

    def query_bank_balance(self, address: Address, denom: Optional[str] = None) -> int:

        denom = denom or self.network_config.fee_denomination

        req = QueryBalanceRequest(
            address=str(address),
            denom=denom,
        )

        resp = self.bank.Balance(req)
        if resp.balance.denom != denom:
            raise InvalidDenominationError(f"Expected {denom}, got {resp.balance.denom}")

        return int(float(resp.balance.amount))

    def tx_bank_send(
            self,
            destination: Address,
            amount: int,
            denom: str,
            sender: Wallet,
            memo: Optional[str] = None,
            gas_limit: Optional[int] = None,
    ) -> TxResponse:

        tx = Transaction()
        tx.add_message(
            msg_send(sender.address(), destination, amount, denom)
        )

        submitted_tx = tx_submit_basic(
            self, tx, sender, gas_limit=gas_limit, memo=memo
        )

        tx_response = self.wait_for_query_tx(submitted_tx.tx_hash)
        return tx_response

    def query_account(self, address: Address) -> Account:

        request = QueryAccountRequest(address=str(address))
        response = self.auth.Account(request)

        account = BaseAccount()
        if not response.account.Is(BaseAccount.DESCRIPTOR):
            raise RuntimeError("Unexpected account type returned from query")
        response.account.Unpack(account)

        return Account(
            address=address,
            number=account.account_number,
            sequence=account.sequence,
        )

    def estimate_gas_for_tx(self, tx: Transaction) -> int:
        estimated_gas = self.gas_strategy.estimate_gas(tx)
        return estimated_gas

    def estimate_fee_from_gas(self, gas_limit: int) -> str:
        fee = math.ceil(gas_limit * self.network_config.fee_minimum_gas_price)
        return f"{fee}{self.network_config.fee_denomination}"

    def estimate_gas_and_fee_for_tx(self, tx: Transaction) -> Tuple[int, str]:
        gas_estimate = self.estimate_gas_for_tx(tx)
        fee = self.estimate_fee_from_gas(gas_estimate)
        return gas_estimate, fee

    def simulate_tx(self, tx: Transaction) -> int:

        if tx.state != TxState.Final:
            raise RuntimeError("Unable to simulate non final transaction")

        req = SimulateRequest(tx=tx.tx)
        resp = self.txs.Simulate(req)

        return int(resp.gas_info.gas_used)

    def broadcast_tx(self, tx: Transaction) -> SubmittedTx:
        # create the broadcast request
        broadcast_req = BroadcastTxRequest(
            tx_bytes=tx.tx.SerializeToString(), mode=BroadcastMode.BROADCAST_MODE_SYNC
        )

        # broadcast the transaction
        resp = self.txs.BroadcastTx(broadcast_req)
        tx_digest = resp.tx_response.txhash

        # check that the response is successful
        initial_tx_response = self._parse_tx_response(resp.tx_response)
        initial_tx_response.ensure_successful()

        return SubmittedTx(self, tx_digest)

    @staticmethod
    def _parse_tx_response(tx_response: Any) -> TxResponse:
        # parse the transaction logs
        logs = []
        for log_data in tx_response.logs:
            events = {}
            for event in log_data.events:
                events[event.type] = {a.key: a.value for a in event.attributes}
            logs.append(
                MessageLog(
                    index=int(log_data.msg_index), log=log_data.msg_index, events=events
                )
            )

        # parse the transaction events
        events = {}
        for event in tx_response.events:
            event_data = events.get(event.type, {})
            for attribute in event.attributes:
                k = attribute.key
                v = attribute.value
                event_data[k] = v
            events[event.type] = event_data

        timestamp = None
        if tx_response.timestamp:
            timestamp = isoparse(tx_response.timestamp)

        return TxResponse(
            hash=str(tx_response.txhash),
            height=int(tx_response.height),
            code=int(tx_response.code),
            gas_wanted=int(tx_response.gas_wanted),
            gas_used=int(tx_response.gas_used),
            raw_log=str(tx_response.raw_log),
            logs=logs,
            events=events,
            timestamp=timestamp,
        )

    def query_params(self, subspace: str, key: str) -> Any:
        req = QueryParamsRequest(subspace=subspace, key=key)
        resp = self.params.Params(req)
        return json.loads(resp.param.value)

    @backoff.on_exception(
        backoff.expo,
        (grpc.RpcError, NotFoundError, RuntimeError),
        max_time=DEFAULT_QUERY_TIMEOUT_SECS,
    )
    def wait_for_query_tx(
            self,
            tx_hash: str,
    ) -> TxResponse:
        return self.query_tx(tx_hash)

    def query_tx(self, tx_hash: str) -> TxResponse:
        req = GetTxRequest(hash=tx_hash)
        try:
            resp = self.txs.GetTx(req)
        except grpc.RpcError as e:
            if "not found" in str(e):
                raise NotFoundError() from e
            raise
        except RuntimeError as e:
            details = str(e)
            if "tx" in details and "not found" in details:
                raise NotFoundError() from e
            raise

        return self._parse_tx_response(resp.tx_response)
