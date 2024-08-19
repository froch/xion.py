from typing import Optional

import grpc

from xionpy.client.exceptions import InvalidDenominationError
from xionpy.client.networks import NetworkConfig
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest
from xionpy.protos.cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankGrpcClient
from xionpy.services.bank.messages import msg_send
from xionpy.services.bank.rest import BankRestClient
from xionpy.services.controller import XionBaseController
from xionpy.services.txs.model import Transaction


class XionBankController(XionBaseController):

    def __init__(self, cfg: NetworkConfig):
        super().__init__(cfg)
        if isinstance(self.binding, grpc.Channel):
            self.client = BankGrpcClient(self.binding)
        else:
            self.client = BankRestClient(self.binding)

    def query_balances(self, address: Address, denom: Optional[str] = None) -> int:
        denom = denom or self.cfg.denom_fee

        req = QueryBalanceRequest(
            address=str(address),
            denom=denom,
        )

        resp = self.client.Balance(req)
        if resp.balance.denom != denom:
            raise InvalidDenominationError(f"Expected {denom}, got {resp.balance.denom}")

        return int(float(resp.balance.amount))

    def tx_send(
            self,
            sender: Address,
            recipient: Address,
            amount: int,
            denom: str,
    ) -> Transaction:
        tx = Transaction()
        tx.add_message(
            msg_send(
                from_address=sender,
                to_address=recipient,
                amount=amount,
                denom=denom,
            )
        )
        return tx
