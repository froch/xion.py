from typing import List, Optional

import grpc

from xionpy.client.exceptions import NotFoundError
from xionpy.client.networks import NetworkConfig
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.staking.v1beta1.query_pb2 import (
    QueryValidatorRequest,
    QueryValidatorsRequest,
)
from xionpy.protos.cosmos.staking.v1beta1.query_pb2_grpc import (
    QueryStub as StakingGrpcClient,
)
from xionpy.services.controller import XionBaseController
from xionpy.services.staking.messages import msg_delegate
from xionpy.services.staking.model import BondStatus, Validator
from xionpy.services.staking.rest import StakingRestClient
from xionpy.services.txs.model import Transaction


class XionStakingController(XionBaseController):

    def __init__(self, cfg: NetworkConfig):
        super().__init__(cfg)
        if isinstance(self.binding, grpc.Channel):
            self.client = StakingGrpcClient(self.binding)
        else:
            self.client = StakingRestClient(self.binding)

    def query_validator_by_moniker(self, moniker: str) -> Validator:
        vals = self.query_validators(BondStatus.UNSPECIFIED)
        val = next((v for v in vals if moniker in v.moniker), None)

        if not val:
            raise NotFoundError(f"Validator {moniker} not found")

        return Validator(
            address=Address(val.address),
            tokens=int(float(val.tokens)),
            moniker=str(val.moniker),
            status=val.status,
        )

    def query_validator_by_address(self, address: Address) -> Validator:
        req = QueryValidatorRequest()
        req.validator_addr = address
        resp = self.client.Validator(req)
        return Validator(
            address=Address(resp.validator.operator_address),
            tokens=int(float(resp.validator.tokens)),
            moniker=str(resp.validator.description.moniker),
            status=BondStatus.from_proto(resp.validator.status),
        )

    def query_validators(
            self, status: Optional[BondStatus] = None
    ) -> List[Validator]:

        filtered_status = status or BondStatus.BONDED
        req = QueryValidatorsRequest()
        if filtered_status != BondStatus.UNSPECIFIED:
            req.status = filtered_status.value

        resp = self.client.Validators(req)

        validators: List[Validator] = []
        for validator in resp.validators:
            validators.append(
                Validator.from_proto(validator)
            )
        return validators

    def tx_delegate(
            self, delegator: Address, validator: Address, amount: int, denom:str
    ) -> Transaction:

        tx = Transaction()
        tx.add_message(
            msg_delegate(
                delegator=delegator,
                validator=validator,
                amount=amount,
                denom=denom,
            )
        )
        return tx
