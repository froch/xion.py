from xionpy.protos.cosmos.staking.v1beta1.query_pb2 import (
    QueryDelegationRequest,
    QueryDelegatorDelegationsRequest,
    QueryDelegatorUnbondingDelegationsRequest,
    QueryDelegatorValidatorRequest,
    QueryDelegatorValidatorsRequest,
    QueryHistoricalInfoRequest,
    QueryParamsRequest,
    QueryPoolRequest,
    QueryRedelegationsRequest,
    QueryUnbondingDelegationRequest,
    QueryValidatorDelegationsRequest,
    QueryValidatorRequest,
    QueryValidatorUnbondingDelegationsRequest,
    QueryValidatorsRequest,
)
from xionpy.services.rest import XionBaseRestClient
from xionpy.services.staking.interface import Staking
from xionpy.services.staking.models import (
    QueryDelegationResponseModel,
    QueryDelegatorDelegationsResponseModel,
    QueryDelegatorUnbondingDelegationsResponseModel,
    QueryDelegatorValidatorResponseModel,
    QueryDelegatorValidatorsResponseModel,
    QueryHistoricalInfoResponseModel,
    QueryParamsResponseModel,
    QueryPoolResponseModel,
    QueryRedelegationsResponseModel,
    QueryUnbondingDelegationResponseModel,
    QueryValidatorDelegationsResponseModel,
    QueryValidatorResponseModel,
    QueryValidatorUnbondingDelegationsResponseModel,
    QueryValidatorsResponseModel,
)


class StakingRestClient(Staking):
    API_URL = "/cosmos/staking/v1beta1"

    def __init__(self, rest_api: XionBaseRestClient) -> None:
        self._rest_api = rest_api

    def Validators(self, request: QueryValidatorsRequest) -> QueryValidatorsResponseModel:
        json_response = self._rest_api.get(f"{self.API_URL}/validators", request)
        return QueryValidatorsResponseModel(**json_response)

    def Validator(self, request: QueryValidatorRequest) -> QueryValidatorResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}",
        )
        return QueryValidatorResponseModel(**json_response)

    def ValidatorDelegations(
            self, request: QueryValidatorDelegationsRequest
    ) -> QueryValidatorDelegationsResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/delegations",
            request,
            ["validatorAddr"],
        )
        return QueryValidatorDelegationsResponseModel(**json_response)

    def ValidatorUnbondingDelegations(
            self, request: QueryValidatorUnbondingDelegationsRequest
    ) -> QueryValidatorUnbondingDelegationsResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/unbonding_delegations",
            request,
            ["validatorAddr"],
        )
        return QueryValidatorUnbondingDelegationsResponseModel(**json_response)

    def Delegation(self, request: QueryDelegationRequest) -> QueryDelegationResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/delegations/{request.delegator_addr}",
        )
        return QueryDelegationResponseModel(**json_response)

    def UnbondingDelegation(
            self, request: QueryUnbondingDelegationRequest
    ) -> QueryUnbondingDelegationResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/delegations/{request.delegator_addr}/unbonding_delegation",
        )
        return QueryUnbondingDelegationResponseModel(**json_response)

    def DelegatorDelegations(
            self, request: QueryDelegatorDelegationsRequest
    ) -> QueryDelegatorDelegationsResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegations/{request.delegator_addr}",
            request,
            ["delegatorAddr"],
        )
        return QueryDelegatorDelegationsResponseModel(**json_response)

    def DelegatorUnbondingDelegations(
            self, request: QueryDelegatorUnbondingDelegationsRequest
    ) -> QueryDelegatorUnbondingDelegationsResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/unbonding_delegations",
            request,
            ["delegatorAddr"],
        )
        return QueryDelegatorUnbondingDelegationsResponseModel(**json_response)

    def Redelegations(
            self, request: QueryRedelegationsRequest
    ) -> QueryRedelegationsResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/redelegations",
            request,
            ["delegatorAddr"],
        )
        return QueryRedelegationsResponseModel(**json_response)

    def DelegatorValidators(
            self, request: QueryDelegatorValidatorsRequest
    ) -> QueryDelegatorValidatorsResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/validators",
            request,
            ["delegatorAddr"],
        )
        return QueryDelegatorValidatorsResponseModel(**json_response)

    def DelegatorValidator(
            self, request: QueryDelegatorValidatorRequest
    ) -> QueryDelegatorValidatorResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/validators/{request.validator_addr}",
        )
        return QueryDelegatorValidatorResponseModel(**json_response)

    def HistoricalInfo(
            self, request: QueryHistoricalInfoRequest
    ) -> QueryHistoricalInfoResponseModel:
        json_response = self._rest_api.get(
            f"{self.API_URL}/historical_info/{request.height}"
        )
        return QueryHistoricalInfoResponseModel(**json_response)

    def Pool(self, request: QueryPoolRequest) -> QueryPoolResponseModel:
        json_response = self._rest_api.get(f"{self.API_URL}/pool")
        return QueryPoolResponseModel(**json_response)

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponseModel:
        json_response = self._rest_api.get(f"{self.API_URL}/params")
        return QueryParamsResponseModel(**json_response)
