import re
from typing import List

from xionpy.protos.cosmos.base.v1beta1.coin_pb2 import Coin


def parse_coins_proto(value: str) -> List[Coin]:

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
