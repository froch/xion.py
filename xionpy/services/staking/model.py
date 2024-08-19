from dataclasses import dataclass
from enum import Enum

from xionpy.crypto.address import Address


class ValidatorStatus(Enum):
    """Validator status."""

    UNSPECIFIED = "BOND_STATUS_UNSPECIFIED"
    BONDED = "BOND_STATUS_BONDED"
    UNBONDING = "BOND_STATUS_UNBONDING"
    UNBONDED = "BOND_STATUS_UNBONDED"

    @classmethod
    def from_proto(cls, value: int) -> "ValidatorStatus":
        """Get the validator status from proto.

        :param value: value
        :raises RuntimeError: Unable to decode validator status
        :return: Validator status
        """
        if value == 0:
            return cls.UNSPECIFIED
        if value == 1:
            return cls.UNBONDED
        if value == 2:
            return cls.UNBONDING
        if value == 3:
            return cls.BONDED
        raise RuntimeError(f"Unable to decode validator status: {value}")


@dataclass
class StakingPosition:
    """Staking positions."""

    validator: Address
    amount: int
    reward: int


@dataclass
class UnbondingPositions:
    """Unbonding positions."""

    validator: Address
    amount: int


@dataclass
class Validator:
    """Validator."""

    address: Address  # the operators address
    tokens: int  # The total amount of tokens for the validator
    moniker: str
    status: ValidatorStatus
