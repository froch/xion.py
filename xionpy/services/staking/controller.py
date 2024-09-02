from typing import List, Optional, Union

import grpc
from google.protobuf.json_format import MessageToDict
from pydantic import TypeAdapter

from xionpy.client import NetworkConfig, XionWallet
from xionpy.client.exceptions import NotFoundError
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest
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
    BondStatusEnum,
    DelegationResponseModel,
    PoolModel,
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
            status: Optional[Union[str, BondStatusEnum]] = None
    ) -> List[ValidatorModel]:
        """
        Query all validators that match the given status.
        :return:
        """

        filtered_status = status or BondStatusEnum.BONDED
        req = QueryValidatorsRequest()
        if filtered_status != BondStatusEnum.UNSPECIFIED:
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

        r = self.query_validators(BondStatusEnum.UNSPECIFIED)
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
        data = MessageToDict(resp.delegation_response, preserving_proto_field_name=True)

        r = TypeAdapter(
            QueryDelegationResponseModel
        ).validate_python(
            {"delegation_response": data}
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

        data = [
            MessageToDict(delegation, preserving_proto_field_name=True)
            for delegation in resp.delegation_responses
        ]

        r = TypeAdapter(
            QueryDelegatorDelegationsResponseModel
        ).validate_python(
            {"delegation_responses": data}
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

        data = [
            MessageToDict(unbonding, preserving_proto_field_name=True)
            for unbonding in resp.unbonding_responses
        ]

        r = TypeAdapter(
            QueryDelegatorUnbondingDelegationsResponseModel
        ).validate_python(
            {"unbonding_responses": data}
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

        data = [
            MessageToDict(redelegation, preserving_proto_field_name=True)
            for redelegation in resp.redelegation_responses
        ]

        r = TypeAdapter(
            QueryRedelegationsResponseModel
        ).validate_python(
            {"redelegation_responses": data}
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
        data = MessageToDict(resp.hist, preserving_proto_field_name=True)

        return TypeAdapter(
            QueryHistoricalInfoResponseModel
        ).validate_python(
            data
        )

    def query_pool(self) -> PoolModel:
        """
        Query the pool info.
        :return:
        """

        req = QueryPoolRequest()
        resp = self.client.Pool(req)
        data = MessageToDict(resp.pool, preserving_proto_field_name=True)

        r = TypeAdapter(
            QueryPoolResponseModel
        ).validate_python(
            {"pool": data}
        )
        return r.pool

    def query_params(self) -> QueryParamsResponseModel:
        """
        Query the staking module parameters.
        :return:
        """

        req = QueryParamsRequest()
        resp = self.client.Params(req)
        data = MessageToDict(resp.params, preserving_proto_field_name=True)

        r =  TypeAdapter(
            QueryParamsResponseModel
        ).validate_python(
            {"params": data}
        )
        return r.params

    def query_validator_delegations(
            self,
            validator_addr: Union[str, Address],
            next_key: Optional[bytes] = None,
            limit: Optional[int] = None,
    ) -> QueryValidatorDelegationsResponseModel:
        """
        Query all delegations for a validator.
        :param validator_addr:
        :param next_key:
        :param limit:
        :return:
        """

        if isinstance(validator_addr, Address):
            validator_addr = str(validator_addr)

        pagination = None
        if next_key or limit:
            pagination = PageRequest()
            if next_key:
                pagination.key = next_key
            if limit:
                pagination.limit = limit

        req = QueryValidatorDelegationsRequest(
            validator_addr=validator_addr,
            pagination=pagination
        )

        resp = self.client.ValidatorDelegations(req)

        delegation_data = [
            MessageToDict(delegation, preserving_proto_field_name=True)
            for delegation in resp.delegation_responses
        ]
        pagination_data = MessageToDict(resp.pagination, preserving_proto_field_name=True)

        return TypeAdapter(
            QueryValidatorDelegationsResponseModel
        ).validate_python({
            "delegation_responses": delegation_data,
            "pagination": pagination_data
        })

    def query_validator_unbonding_delegations(
            self,
            validator_addr: Union[str, Address],
            next_key: Optional[bytes] = None,
            limit: Optional[int] = None,
    ) -> QueryValidatorUnbondingDelegationsResponseModel:
        """
        Query all unbonding delegations for a validator.
        :param validator_addr:
        :param next_key:
        :param limit:
        :return:
        """

        if isinstance(validator_addr, Address):
            validator_addr = str(validator_addr)

        pagination = None
        if next_key or limit:
            pagination = PageRequest()
            if next_key:
                pagination.key = next_key
            if limit:
                pagination.limit = limit

        req = QueryValidatorUnbondingDelegationsRequest(
            validator_addr=validator_addr,
            pagination=pagination,
        )
        resp = self.client.ValidatorUnbondingDelegations(req)

        unbonding_responses_data = [
            MessageToDict(unbonding, preserving_proto_field_name=True)
            for unbonding in resp.unbonding_responses
        ]
        pagination_data = MessageToDict(resp.pagination, preserving_proto_field_name=True)

        return TypeAdapter(
            QueryValidatorUnbondingDelegationsResponseModel
        ).validate_python({
            "unbonding_responses": unbonding_responses_data,
            "pagination": pagination_data
        })
