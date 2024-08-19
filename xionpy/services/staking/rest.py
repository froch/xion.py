from google.protobuf.json_format import Parse

from xionpy.protos.cosmos.staking.v1beta1.query_pb2 import (
    QueryDelegationRequest,
    QueryDelegationResponse,
    QueryDelegatorDelegationsRequest,
    QueryDelegatorDelegationsResponse,
    QueryDelegatorUnbondingDelegationsRequest,
    QueryDelegatorUnbondingDelegationsResponse,
    QueryDelegatorValidatorRequest,
    QueryDelegatorValidatorResponse,
    QueryDelegatorValidatorsRequest,
    QueryDelegatorValidatorsResponse,
    QueryHistoricalInfoRequest,
    QueryHistoricalInfoResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QueryPoolRequest,
    QueryPoolResponse,
    QueryRedelegationsRequest,
    QueryRedelegationsResponse,
    QueryUnbondingDelegationRequest,
    QueryUnbondingDelegationResponse,
    QueryValidatorDelegationsRequest,
    QueryValidatorDelegationsResponse,
    QueryValidatorRequest,
    QueryValidatorResponse,
    QueryValidatorUnbondingDelegationsRequest,
    QueryValidatorUnbondingDelegationsResponse,
    QueryValidatorsRequest,
    QueryValidatorsResponse,
)
from xionpy.services.rest import XionBaseRestClient
from xionpy.services.staking.interface import Staking


class StakingRestClient(Staking):

    API_URL = "/cosmos/staking/v1beta1"

    def __init__(self, rest_api: XionBaseRestClient) -> None:
        self._rest_api = rest_api

    def Validators(self, request: QueryValidatorsRequest) -> QueryValidatorsResponse:
        json_response = self._rest_api.get(f"{self.API_URL}/validators", request)
        return Parse(json_response, QueryValidatorsResponse())

    def Validator(self, request: QueryValidatorRequest) -> QueryValidatorResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}",
        )
        return Parse(json_response, QueryValidatorResponse())

    def ValidatorDelegations(
        self, request: QueryValidatorDelegationsRequest
    ) -> QueryValidatorDelegationsResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/delegations",
            request,
            ["validatorAddr"],
        )
        return Parse(json_response, QueryValidatorDelegationsResponse())

    def ValidatorUnbondingDelegations(
        self, request: QueryValidatorUnbondingDelegationsRequest
    ) -> QueryValidatorUnbondingDelegationsResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/unbonding_delegations",
            request,
            ["validatorAddr"],
        )
        return Parse(json_response, QueryValidatorUnbondingDelegationsResponse())

    def Delegation(self, request: QueryDelegationRequest) -> QueryDelegationResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/delegations/{request.delegator_addr}",
        )
        return Parse(json_response, QueryDelegationResponse())

    def UnbondingDelegation(
        self, request: QueryUnbondingDelegationRequest
    ) -> QueryUnbondingDelegationResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/delegations/{request.delegator_addr}/unbonding_delegation",
        )
        return Parse(json_response, QueryUnbondingDelegationResponse())

    def DelegatorDelegations(
        self, request: QueryDelegatorDelegationsRequest
    ) -> QueryDelegatorDelegationsResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegations/{request.delegator_addr}",
            request,
            ["delegatorAddr"],
        )
        return Parse(json_response, QueryDelegatorDelegationsResponse())

    def DelegatorUnbondingDelegations(
        self, request: QueryDelegatorUnbondingDelegationsRequest
    ) -> QueryDelegatorUnbondingDelegationsResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/unbonding_delegations",
            request,
            ["delegatorAddr"],
        )
        return Parse(json_response, QueryDelegatorUnbondingDelegationsResponse())

    def Redelegations(
        self, request: QueryRedelegationsRequest
    ) -> QueryRedelegationsResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/redelegations",
            request,
            ["delegatorAddr"],
        )
        return Parse(json_response, QueryRedelegationsResponse())

    def DelegatorValidators(
        self, request: QueryDelegatorValidatorsRequest
    ) -> QueryDelegatorValidatorsResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/validators",
            request,
            ["delegatorAddr"],
        )
        return Parse(json_response, QueryDelegatorValidatorsResponse())

    def DelegatorValidator(
        self, request: QueryDelegatorValidatorRequest
    ) -> QueryDelegatorValidatorResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/validators/{request.validator_addr}",
        )
        return Parse(json_response, QueryDelegatorValidatorResponse())

    def HistoricalInfo(
        self, request: QueryHistoricalInfoRequest
    ) -> QueryHistoricalInfoResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/historical_info/{request.height}"
        )
        return Parse(json_response, QueryHistoricalInfoResponse())

    def Pool(self, request: QueryPoolRequest) -> QueryPoolResponse:
        json_response = self._rest_api.get(f"{self.API_URL}/pool")
        return Parse(json_response, QueryPoolResponse())

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        json_response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(json_response, QueryParamsResponse())
