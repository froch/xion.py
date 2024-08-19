from typing import List, Optional

import grpc

from xionpy.client.networks import NetworkConfig
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.staking.v1beta1.query_pb2 import QueryValidatorsRequest
from xionpy.protos.cosmos.staking.v1beta1.query_pb2_grpc import (
    QueryStub as StakingGrpcClient,
)
from xionpy.services.controller import XionBaseController
from xionpy.services.staking.messages import msg_delegate
from xionpy.services.staking.model import Validator, ValidatorStatus
from xionpy.services.staking.rest import StakingRestClient
from xionpy.services.txs.model import Transaction


class XionStakingController(XionBaseController):

    def __init__(self, cfg: NetworkConfig):
        super().__init__(cfg)
        if isinstance(self.binding, grpc.Channel):
            self.client = StakingGrpcClient(self.binding)
        else:
            self.client = StakingRestClient(self.binding)

    def query_validators(
            self, status: Optional[ValidatorStatus] = None
    ) -> List[Validator]:

        filtered_status = status or ValidatorStatus.BONDED
        req = QueryValidatorsRequest()
        if filtered_status != ValidatorStatus.UNSPECIFIED:
            req.status = filtered_status.value

        resp = self.client.Validators(req)

        validators: List[Validator] = []
        for validator in resp.validators:
            validators.append(
                Validator(
                    address=Address(validator.operator_address),
                    tokens=int(float(validator.tokens)),
                    moniker=str(validator.description.moniker),
                    status=ValidatorStatus.from_proto(validator.status),
                )
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
