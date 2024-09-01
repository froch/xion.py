from abc import ABC, abstractmethod

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


class Bank(ABC):
    """Bank abstract class."""

    @abstractmethod
    def Balance(self, request: QueryBalanceRequest) -> QueryBalanceResponse:
        pass

    @abstractmethod
    def AllBalances(self, request: QueryAllBalancesRequest) -> QueryAllBalancesResponse:
        pass

    @abstractmethod
    def TotalSupply(self, request: QueryTotalSupplyRequest) -> QueryTotalSupplyResponse:
        pass

    @abstractmethod
    def SupplyOf(self, request: QuerySupplyOfRequest) -> QuerySupplyOfResponse:
        pass

    @abstractmethod
    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        pass

    @abstractmethod
    def DenomMetadata(
            self, request: QueryDenomMetadataRequest
    ) -> QueryDenomMetadataResponse:
        pass

    @abstractmethod
    def DenomsMetadata(
            self, request: QueryDenomsMetadataRequest
    ) -> QueryDenomsMetadataResponse:
        pass

    @abstractmethod
    def DenomOwners(
            self, request: QueryDenomOwnersRequest
    ) -> QueryDenomOwnersResponse:
        pass

    @abstractmethod
    def SendEnabled(
            self, request: QuerySendEnabledRequest
    ) -> QuerySendEnabledResponse:
        pass

    @abstractmethod
    def SpendableBalanceByDenom(
            self, request: QuerySpendableBalanceByDenomRequest
    ) -> QuerySpendableBalanceByDenomResponse:
        pass

    @abstractmethod
    def SpendableBalances(
            self, request: QuerySpendableBalancesRequest
    ) -> QuerySpendableBalancesResponse:
        pass
