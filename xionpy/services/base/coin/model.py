import re

from pydantic import BaseModel


class Coin(BaseModel):
    denom: str
    amount: str

    @classmethod
    def from_proto(cls, coin):
        return cls(denom=coin.denom, amount=coin.amount)

    @classmethod
    def from_list(cls, value: str):
        coins = []

        parts = re.split(r",\s*", value)
        for part in parts:
            part = part.strip()
            if part == "":
                continue

            match = re.match(r"^(\d+)(.+)$", part)
            if match is None:
                raise RuntimeError(f"Unable to parse value {part}")

            # extract out the groups
            amount, denom = match.groups()
            coins.append(Coin(amount=amount, denom=denom))

        return coins
