from typing import List, Optional, Union

import grpc
from google.protobuf.json_format import MessageToDict
from pydantic import TypeAdapter

from xionpy.client import NetworkConfig, XionWallet
from xionpy.client.exceptions import NotFoundError
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.crypto.ed25519 import (  # noqa: F401  # pylint: disable=unused-import
    keys_pb2,
)
from xionpy.protos.cosmos.staking.v1beta1.query_pb2 import (
    QueryDelegationRequest,
    QueryDelegatorDelegationsRequest,
    QueryDelegatorUnbondingDelegationsRequest,
    QueryHistoricalInfoRequest,
    QueryParamsRequest,
    QueryPoolRequest,
    QueryRedelegationsRequest,
    QueryValidatorDelegationsRequest,
    QueryValidatorRequest,
    QueryValidatorUnbondingDelegationsRequest,
    QueryValidatorsRequest,
)
from xionpy.protos.cosmos.staking.v1beta1.query_pb2_grpc import (
    QueryStub as StakingGrpcClient,
)
from xionpy.services.controller import XionBaseController
from xionpy.services.staking.models import (
    BondStatus,
    DelegationResponseModel,
    QueryDelegationResponseModel,
    QueryDelegatorDelegationsResponseModel,
    QueryDelegatorUnbondingDelegationsResponseModel,
    QueryHistoricalInfoResponseModel,
    QueryParamsResponseModel,
    QueryPoolResponseModel,
    QueryRedelegationsResponseModel,
    QueryValidatorDelegationsResponseModel,
    QueryValidatorResponseModel,
    QueryValidatorUnbondingDelegationsResponseModel,
    QueryValidatorsResponseModel,
    RedelegationResponseModel,
    UnbondingDelegationModel,
    ValidatorModel,
)
from xionpy.services.staking.rest import StakingRestClient


class XionStakingController(XionBaseController):

    def __init__(self, cfg: NetworkConfig, wallet: XionWallet):
        super().__init__(cfg, wallet)
        if isinstance(self.binding, grpc.Channel):
            self.client = StakingGrpcClient(self.binding)
        else:
            self.client = StakingRestClient(self.binding)

    def query_validator(
            self,
            validator_addr: str
    ) -> ValidatorModel:
        """
        Query validator info for given validator operator address.
        :return:
        """

        req = QueryValidatorRequest(validator_addr=validator_addr)
        resp = self.client.Validator(req)
        validator_data = MessageToDict(resp.validator, preserving_proto_field_name=True)

        r = TypeAdapter(
            QueryValidatorResponseModel
        ).validate_python(
            {"validator": validator_data}
        )
        return r.validator

    def query_validators(
            self,
            status: Optional[Union[str, BondStatus]] = None
    ) -> List[ValidatorModel]:
        """
        Query all validators that match the given status.
        :return:
        """

        filtered_status = status or BondStatus.BONDED
        req = QueryValidatorsRequest()
        if filtered_status != BondStatus.UNSPECIFIED:
            req.status = filtered_status.value

        resp = self.client.Validators(req)
        validators_data = [
            MessageToDict(validator, preserving_proto_field_name=True)
            for validator in resp.validators
        ]

        r = TypeAdapter(
            QueryValidatorsResponseModel
        ).validate_python(
            {"validators": validators_data}
        )
        return r.validators

    def query_validator_by_moniker(
            self,
            moniker: str,
    ) -> ValidatorModel:
        """
        Query validator info for given validator moniker.
        :param moniker: string to look for
        :return:
        """

        r = self.query_validators(BondStatus.UNSPECIFIED)
        val = next((v for v in r if moniker in v.description.moniker), None)

        if not val:
            raise NotFoundError(f"Validator with moniker {moniker} not found")

        return val

    def query_delegation(
            self,
            delegator_addr: Union[str, Address],
            validator_addr: Union[str, Address],
    ) -> DelegationResponseModel:
        """
        Query delegate info for given validator delegator pair.
        :return:
        """

        if isinstance(delegator_addr, Address):
            delegator_addr = str(delegator_addr)
        if isinstance(validator_addr, Address):
            validator_addr = str(validator_addr)

        req = QueryDelegationRequest(delegator_addr=delegator_addr, validator_addr=validator_addr)
        resp = self.client.Delegation(req)
        delegation_data = MessageToDict(resp.delegation_response, preserving_proto_field_name=True)

        r = TypeAdapter(
            QueryDelegationResponseModel
        ).validate_python(
            {"delegation_response": delegation_data}
        )
        return r.delegation_response

    def query_delegator_delegations(
            self,
            delegator_addr: Union[str, Address],
    ) -> List[DelegationResponseModel]:
        """
        Query all delegations for a delegator.
        :return:
        """

        if isinstance(delegator_addr, Address):
            delegator_addr = str(delegator_addr)

        req = QueryDelegatorDelegationsRequest(delegator_addr=delegator_addr)
        resp = self.client.DelegatorDelegations(req)

        delegations_data = [
            MessageToDict(delegation, preserving_proto_field_name=True)
            for delegation in resp.delegation_responses
        ]

        r = TypeAdapter(
            QueryDelegatorDelegationsResponseModel
        ).validate_python(
            {"delegation_responses": delegations_data}
        )
        return r.delegation_responses

    def query_delegator_unbonding_delegations(
            self,
            delegator_addr: Union[str, Address],
    ) -> List[UnbondingDelegationModel]:
        """
        Query all unbonding delegations for a delegator.
        :return:
        """

        if isinstance(delegator_addr, Address):
            delegator_addr = str(delegator_addr)

        req = QueryDelegatorUnbondingDelegationsRequest(delegator_addr=delegator_addr)
        resp = self.client.DelegatorUnbondingDelegations(req)

        unbonding_data = [
            MessageToDict(unbonding, preserving_proto_field_name=True)
            for unbonding in resp.unbonding_responses
        ]

        r = TypeAdapter(
            QueryDelegatorUnbondingDelegationsResponseModel
        ).validate_python(
            {"unbonding_responses": unbonding_data}
        )
        return r.unbonding_responses

    def query_redelegations(
            self,
            delegator_addr: Union[str, Address],
    ) -> List[RedelegationResponseModel]:
        """
        Query redelegations of given address.
        :return:
        """

        if isinstance(delegator_addr, Address):
            delegator_addr = str(delegator_addr)

        req = QueryRedelegationsRequest(delegator_addr=delegator_addr)
        resp = self.client.Redelegations(req)

        redelegations_data = [
            MessageToDict(redelegation, preserving_proto_field_name=True)
            for redelegation in resp.redelegation_responses
        ]

        r = TypeAdapter(
            QueryRedelegationsResponseModel
        ).validate_python(
            {"redelegation_responses": redelegations_data}
        )
        return r.redelegation_responses

    def query_historical_info(
            self,
            height: int,
    ) -> QueryHistoricalInfoResponseModel:
        """
        Query the historical info for given height.
        :return:
        """

        req = QueryHistoricalInfoRequest(height=height)
        resp = self.client.HistoricalInfo(req)

        historical_info_data = MessageToDict(resp.hist, preserving_proto_field_name=True)

        return TypeAdapter(
            QueryHistoricalInfoResponseModel
        ).validate_python(
            historical_info_data
        )

    def query_pool(self) -> QueryPoolResponseModel:
        req = QueryPoolRequest()
        resp = self.client.Pool(req)
        pool_data = MessageToDict(resp.pool, preserving_proto_field_name=True)
        return TypeAdapter(QueryPoolResponseModel).validate_python({"pool": pool_data})

    def query_params(self) -> QueryParamsResponseModel:
        req = QueryParamsRequest()
        resp = self.client.Params(req)
        params_data = MessageToDict(resp.params, preserving_proto_field_name=True)
        return TypeAdapter(QueryParamsResponseModel).validate_python({"params": params_data})

    def query_validator_delegations(
            self,
            validator_addr: str,
    ) -> QueryValidatorDelegationsResponseModel:
        req = QueryValidatorDelegationsRequest(validator_addr=validator_addr)
        resp = self.client.ValidatorDelegations(req)
        delegation_responses_data = [MessageToDict(delegation, preserving_proto_field_name=True) for
                                     delegation in resp.delegation_responses]
        pagination_data = MessageToDict(resp.pagination, preserving_proto_field_name=True)
        return TypeAdapter(QueryValidatorDelegationsResponseModel).validate_python({
            "delegation_responses": delegation_responses_data,
            "pagination": pagination_data
        })

    def query_validator_unbonding_delegations(
            self,
            validator_addr: str,
    ) -> QueryValidatorUnbondingDelegationsResponseModel:
        req = QueryValidatorUnbondingDelegationsRequest(validator_addr=validator_addr)
        resp = self.client.ValidatorUnbondingDelegations(req)
        unbonding_responses_data = [MessageToDict(unbonding, preserving_proto_field_name=True) for
                                    unbonding in resp.unbonding_responses]
        pagination_data = MessageToDict(resp.pagination, preserving_proto_field_name=True)
        return TypeAdapter(QueryValidatorUnbondingDelegationsResponseModel).validate_python({
            "unbonding_responses": unbonding_responses_data,
            "pagination": pagination_data
        })
