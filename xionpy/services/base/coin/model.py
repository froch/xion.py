import re

from pydantic import BaseModel

from xionpy.protos.cosmos.base.v1beta1.coin_pb2 import Coin


class CoinModel(BaseModel):
    denom: str
    amount: int

    @classmethod
    def from_proto(cls, coin):
        return cls(denom=coin.denom, amount=coin.amount)

    @classmethod
    def to_proto(cls, value: str):
        value = value.strip()
        if value == "":
            raise ValueError("Empty Coin; can't convert to proto")

        match = re.match(r"^(\d+)(.+)$", value)
        if match is None:
            raise ValueError(f"Unable to convert Coin to proto: {value}")

        amount, denom = match.groups()
        return Coin(denom=denom, amount=amount)

    @classmethod
    def to_proto_list(cls, value: str):
        coins = []

        parts = re.split(r",\s*", value)
        for part in parts:
            c = cls.to_proto(part)
            coins.append(c)

        return coins
