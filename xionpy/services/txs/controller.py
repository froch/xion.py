import math
from typing import Any, Tuple

import backoff
import grpc
from dateutil.parser import isoparse

from xionpy.client.exceptions import NotFoundError
from xionpy.client.networks import NetworkConfig
from xionpy.protos.cosmos.tx.v1beta1.service_pb2 import (
    BroadcastMode,
    BroadcastTxRequest,
    GetTxRequest,
    SimulateRequest,
)
from xionpy.services.controller import XionBaseController
from xionpy.services.txs.gas import GasStrategy
from xionpy.services.txs.model import (
    MessageLog,
    SubmittedTx,
    Transaction,
    TxResponse,
    TxState,
)
from xionpy.protos.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub as TxsGrpcClient
from xionpy.services.txs.rest import TxsRestClient


DEFAULT_QUERY_TIMEOUT_SECS = 30
DEFAULT_QUERY_INTERVAL_SECS = 2

class XionTxsController(XionBaseController):

    def __init__(
            self,
            cfg: NetworkConfig,
            gas_strategy: GasStrategy,
     ):
        super().__init__(cfg)
        self.gas_strategy = gas_strategy
        if isinstance(self.binding, grpc.Channel):
            self.client = TxsGrpcClient(self.binding)
        else:
            self.client = TxsRestClient(self.binding)


    def estimate_gas(self, tx: Transaction) -> int:
        estimated_gas = self.gas_strategy.estimate_gas(tx)
        return estimated_gas

    def estimate_fee_from_gas(self, gas_limit: int) -> str:
        fee = math.ceil(gas_limit * self.cfg.min_fee)
        return f"{fee}{self.cfg.denom_fee}"

    def estimate_gas_and_fee(self, tx: Transaction) -> Tuple[int, str]:
        gas_estimate = self.estimate_gas(tx)
        fee = self.estimate_fee_from_gas(gas_estimate)
        return gas_estimate, fee

    def simulate(self, tx: Transaction) -> int:
        if tx.state != TxState.Final:
            raise RuntimeError("Unable to simulate non final transaction")

        req = SimulateRequest(tx=tx.tx)
        resp = self.client.Simulate(req)

        return int(resp.gas_info.gas_used)

    def broadcast(self, tx: Transaction) -> SubmittedTx:
        # broadcast the transaction
        broadcast_req = BroadcastTxRequest(
            tx_bytes=tx.tx.SerializeToString(), mode=BroadcastMode.BROADCAST_MODE_SYNC
        )
        resp = self.client.BroadcastTx(broadcast_req)
        tx_digest = resp.tx_response.txhash

        # check that the initial broadcast is successful
        # -- submitting the tx might be OK
        # -- but the actual tx might fail; the caller should check it
        initial_tx_response = self.parse_tx_response(resp.tx_response)
        initial_tx_response.ensure_successful()

        return SubmittedTx(self, tx_digest)

    @staticmethod
    def parse_tx_response(tx_response: Any) -> TxResponse:
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

    @backoff.on_exception(
        backoff.expo,
        (grpc.RpcError, NotFoundError, RuntimeError),
        max_time=DEFAULT_QUERY_TIMEOUT_SECS,
    )
    def wait_for_tx(
            self,
            tx_hash: str,
    ) -> TxResponse:
        return self.query_tx(tx_hash)

    def query_tx(self, tx_hash: str) -> TxResponse:
        req = GetTxRequest(hash=tx_hash)
        try:
            resp = self.client.GetTx(req)
        except grpc.RpcError as e:
            if "not found" in str(e):
                raise NotFoundError() from e
            raise
        except RuntimeError as e:
            details = str(e)
            if "tx" in details and "not found" in details:
                raise NotFoundError() from e
            raise

        return self.parse_tx_response(resp.tx_response)
