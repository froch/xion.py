from xionpy.crypto.address import Address
from xionpy.protos.cosmos.staking.v1beta1.tx_pb2 import (
    MsgBeginRedelegate,
    MsgDelegate,
    MsgUndelegate,
)
from xionpy.services.base.coin.model import Coin


def msg_delegate(
        delegator: Address, validator: Address, amount: int, denom: str
) -> MsgDelegate:
    return MsgDelegate(
        delegator_address=str(delegator),
        validator_address=str(validator),
        amount=Coin(
            amount=str(amount),
            denom=denom,
        ),
    )


def msg_redelegate(
        delegator_address: Address,
        validator_src_address: Address,
        validator_dst_address: Address,
        amount: int,
        denom: str,
) -> MsgBeginRedelegate:
    return MsgBeginRedelegate(
        delegator_address=str(delegator_address),
        validator_src_address=str(validator_src_address),
        validator_dst_address=str(validator_dst_address),
        amount=Coin(
            amount=str(amount),
            denom=str(denom),
        ),
    )


def msg_undelegate(
        delegator_address: Address, validator_address: Address, amount: int, denom: str
) -> MsgUndelegate:
    return MsgUndelegate(
        delegator_address=str(delegator_address),
        validator_address=str(validator_address),
        amount=Coin(
            amount=str(amount),
            denom=str(denom),
        ),
    )
