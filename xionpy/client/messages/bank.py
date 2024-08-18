from xionpy.crypto.address import Address
from xionpy.protos.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from xionpy.protos.cosmos.base.v1beta1.coin_pb2 import Coin


def msg_send(
        from_address: Address,
        to_address: Address,
        amount: int,
        denom: str
) -> MsgSend:

    msg = MsgSend(
        from_address=str(from_address),
        to_address=str(to_address),
        amount=[Coin(amount=str(amount), denom=denom)],
    )

    return msg
