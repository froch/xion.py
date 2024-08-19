from pydantic import BaseModel


class Coin(BaseModel):
    denom: str
    amount: str

    @classmethod
    def from_proto(cls, coin):
        return cls(denom=coin.denom, amount=coin.amount)
