import certifi
import grpc
from typing import Optional

from xionpy.bank.rest_client import BankRestClient
from xionpy.client.config import NetworkConfig
from xionpy.client.gas import GasStrategy, SimulationGasStrategy
from xionpy.client.urls import parse_url, Protocol
from xionpy.common.rest_client import RestClient
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest
from xionpy.protos.cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankGrpcClient

DEFAULT_QUERY_TIMEOUT_SECS = 15
DEFAULT_QUERY_INTERVAL_SECS = 2

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
        self._network_config = cfg
        self._gas_strategy: GasStrategy = SimulationGasStrategy(self)

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

            self.bank = BankGrpcClient(grpc_client)
        else:
            rest_client = RestClient(parsed_url.rest_url)
            self.bank = BankRestClient(rest_client)

    def query_bank_balance(self, address: Address, denom: Optional[str] = None) -> int:
        """Query bank balance.

        :param address: address
        :param denom: denom, defaults to None
        :return: bank balance
        """
        denom = denom or self._network_config.fee_denomination

        req = QueryBalanceRequest(
            address=str(address),
            denom=denom,
        )

        resp = self.bank.Balance(req)
        assert resp.balance.denom == denom  # sanity check

        return int(float(resp.balance.amount))
