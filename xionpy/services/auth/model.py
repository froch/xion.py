from dataclasses import dataclass

from xionpy.crypto.address import Address


@dataclass
class Account:
    address: Address
    number: int
    sequence: int
