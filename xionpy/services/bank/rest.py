from google.protobuf.json_format import Parse

from xionpy.protos.cosmos.bank.v1beta1.query_pb2 import (
    QueryAllBalancesRequest,
    QueryAllBalancesResponse,
    QueryBalanceRequest,
    QueryBalanceResponse,
    QueryDenomMetadataRequest,
    QueryDenomMetadataResponse,
    QueryDenomOwnersRequest,
    QueryDenomOwnersResponse,
    QueryDenomsMetadataRequest,
    QueryDenomsMetadataResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QuerySendEnabledRequest,
    QuerySendEnabledResponse,
    QuerySpendableBalanceByDenomRequest,
    QuerySpendableBalanceByDenomResponse,
    QuerySpendableBalancesRequest,
    QuerySpendableBalancesResponse,
    QuerySupplyOfRequest,
    QuerySupplyOfResponse,
    QueryTotalSupplyRequest,
    QueryTotalSupplyResponse,
)
from xionpy.services.bank.interface import Bank
from xionpy.services.rest import XionBaseRestClient


class BankRestClient(Bank):

    API_URL = "/cosmos/bank/v1beta1"

    def __init__(self, rest_api: XionBaseRestClient):
        self._rest_api = rest_api

    def Balance(self, request: QueryBalanceRequest) -> QueryBalanceResponse:
        response = self._rest_api.get(
            f"{self.API_URL}/balances/{request.address}/by_denom?denom={request.denom}",
            request,
            ["address", "denom"],
        )
        return Parse(response, QueryBalanceResponse())

    def AllBalances(self, request: QueryAllBalancesRequest) -> QueryAllBalancesResponse:
        response = self._rest_api.get(
            f"{self.API_URL}/balances/{request.address}", request, ["address"]
        )
        return Parse(response, QueryAllBalancesResponse())

    def TotalSupply(self, request: QueryTotalSupplyRequest) -> QueryTotalSupplyResponse:
        response = self._rest_api.get(f"{self.API_URL}/supply", request)
        return Parse(response, QueryTotalSupplyResponse())

    def SupplyOf(self, request: QuerySupplyOfRequest) -> QuerySupplyOfResponse:
        response = self._rest_api.get(f"{self.API_URL}/supply/by_denom?denom={request.denom}")
        return Parse(response, QuerySupplyOfResponse())

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(response, QueryParamsResponse())

    def DenomMetadata(
            self, request: QueryDenomMetadataRequest
    ) -> QueryDenomMetadataResponse:
        response = self._rest_api.get(f"{self.API_URL}/denoms_metadata/{request.denom}")
        return Parse(response, QueryDenomMetadataResponse())

    def DenomsMetadata(
            self, request: QueryDenomsMetadataRequest
    ) -> QueryDenomsMetadataResponse:
        response = self._rest_api.get(f"{self.API_URL}/denoms_metadata", request)
        return Parse(response, QueryDenomsMetadataResponse())

    def DenomOwners(
            self, request: QueryDenomOwnersRequest
    ) -> QueryDenomOwnersResponse:
        response = self._rest_api.get(f"{self.API_URL}/denom_owners/{request.denom}")
        return Parse(response, QueryDenomOwnersResponse())

    def SendEnabled(
            self, request: QuerySendEnabledRequest
    ) -> QuerySendEnabledResponse:
        response = self._rest_api.get(f"{self.API_URL}/send_enabled")
        return Parse(response, QuerySendEnabledResponse())

    def SpendableBalanceByDenom(
            self, request: QuerySpendableBalanceByDenomRequest
    ) -> QuerySpendableBalanceByDenomResponse:
        response = self._rest_api.get(
            f"{self.API_URL}/spendable_balances/{request.address}/by_denom?denom={request.denom}",
            request,
            ["address", "denom"],
        )
        return Parse(response, QuerySpendableBalanceByDenomResponse())

    def SpendableBalances(
            self, request: QuerySpendableBalancesRequest
    ) -> QuerySpendableBalancesResponse:
        response = self._rest_api.get(
            f"{self.API_URL}/spendable_balances/{request.address}", request, ["address"]
        )
        return Parse(response, QuerySpendableBalancesResponse())
