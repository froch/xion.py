from datetime import datetime, timedelta
from enum import Enum
from typing import List

from pydantic import BaseModel


class BondStatus(Enum):
    UNSPECIFIED = "BOND_STATUS_UNSPECIFIED"
    UNBONDED = "BOND_STATUS_UNBONDED"
    UNBONDING = "BOND_STATUS_UNBONDING"
    BONDED = "BOND_STATUS_BONDED"

    @classmethod
    def from_proto(cls, value: int) -> "BondStatus":
        if value == 0:
            return cls.UNSPECIFIED
        if value == 1:
            return cls.UNBONDED
        if value == 2:
            return cls.UNBONDING
        if value == 3:
            return cls.BONDED
        raise RuntimeError(f"Unable to decode bond status: {value}")

class Infraction(Enum):
    UNSPECIFIED = "INFRACTION_UNSPECIFIED"
    DOUBLE_SIGN = "INFRACTION_DOUBLE_SIGN"
    DOWNTIME = "INFRACTION_DOWNTIME"

    @classmethod
    def from_proto(cls, value: int) -> "Infraction":
        if value == 0:
            return cls.UNSPECIFIED
        if value == 1:
            return cls.DOUBLE_SIGN
        if value == 2:
            return cls.DOWNTIME
        raise RuntimeError(f"Unable to decode infraction: {value}")

class Header(BaseModel):

    @classmethod
    def from_proto(cls, proto):
        return cls()

class CommissionRates(BaseModel):
    rate: str
    max_rate: str
    max_change_rate: str

    @classmethod
    def from_proto(cls, proto):
        return cls(
            rate=proto.rate,
            max_rate=proto.max_rate,
            max_change_rate=proto.max_change_rate,
        )

class Commission(BaseModel):
    commission_rates: CommissionRates
    update_time: datetime

    @classmethod
    def from_proto(cls, proto):
        return cls(
            commission_rates=CommissionRates.from_proto(proto.commission_rates),
            update_time=proto.update_time.ToDatetime(),
        )

class Description(BaseModel):
    moniker: str
    identity: str
    website: str
    security_contact: str
    details: str

    @classmethod
    def from_proto(cls, proto):
        return cls(
            moniker=proto.moniker,
            identity=proto.identity,
            website=proto.website,
            security_contact=proto.security_contact,
            details=proto.details,
        )

class Validator(BaseModel):
    operator_address: str
    consensus_pubkey: bytes
    jailed: bool
    status: BondStatus
    tokens: str
    delegator_shares: str
    description: Description
    unbonding_height: int
    unbonding_time: datetime
    commission: Commission
    min_self_delegation: str
    unbonding_on_hold_ref_count: int
    unbonding_ids: List[int]

    @classmethod
    def from_proto(cls, proto):
        return cls(
            operator_address=proto.operator_address,
            consensus_pubkey=proto.consensus_pubkey,
            jailed=proto.jailed,
            status=BondStatus.from_proto(proto.status),
            tokens=proto.tokens,
            delegator_shares=proto.delegator_shares,
            description=Description.from_proto(proto.description),
            unbonding_height=proto.unbonding_height,
            unbonding_time=proto.unbonding_time.ToDatetime(),
            commission=Commission.from_proto(proto.commission),
            min_self_delegation=proto.min_self_delegation,
            unbonding_on_hold_ref_count=proto.unbonding_on_hold_ref_count,
            unbonding_ids=list(proto.unbonding_ids),
        )

class HistoricalInfo(BaseModel):
    header: Header
    valset: List[Validator]

    @classmethod
    def from_proto(cls, proto):
        return cls(
            header=Header.from_proto(proto.header),
            valset=[Validator.from_proto(v) for v in proto.valset],
        )

class ValAddresses(BaseModel):
    addresses: List[str]

    @classmethod
    def from_proto(cls, proto):
        return cls(
            addresses=list(proto.addresses)
        )

class DVPair(BaseModel):
    delegator_address: str
    validator_address: str

    @classmethod
    def from_proto(cls, proto):
        return cls(
            delegator_address=proto.delegator_address,
            validator_address=proto.validator_address,
        )

class DVPairs(BaseModel):
    pairs: List[DVPair]

    @classmethod
    def from_proto(cls, proto):
        return cls(
            pairs=[DVPair.from_proto(pair) for pair in proto.pairs],
        )

class DVVTriplet(BaseModel):
    delegator_address: str
    validator_src_address: str
    validator_dst_address: str

    @classmethod
    def from_proto(cls, proto):
        return cls(
            delegator_address=proto.delegator_address,
            validator_src_address=proto.validator_src_address,
            validator_dst_address=proto.validator_dst_address,
        )

class DVVTriplets(BaseModel):
    triplets: List[DVVTriplet]

    @classmethod
    def from_proto(cls, proto):
        return cls(
            triplets=[DVVTriplet.from_proto(triplet) for triplet in proto.triplets],
        )

class Delegation(BaseModel):
    delegator_address: str
    validator_address: str
    shares: str

    @classmethod
    def from_proto(cls, proto):
        return cls(
            delegator_address=proto.delegator_address,
            validator_address=proto.validator_address,
            shares=proto.shares,
        )

class UnbondingDelegationEntry(BaseModel):
    creation_height: int
    completion_time: datetime
    initial_balance: str
    balance: str
    unbonding_id: int
    unbonding_on_hold_ref_count: int

    @classmethod
    def from_proto(cls, proto):
        return cls(
            creation_height=proto.creation_height,
            completion_time=proto.completion_time.ToDatetime(),
            initial_balance=proto.initial_balance,
            balance=proto.balance,
            unbonding_id=proto.unbonding_id,
            unbonding_on_hold_ref_count=proto.unbonding_on_hold_ref_count,
        )

class UnbondingDelegation(BaseModel):
    delegator_address: str
    validator_address: str
    entries: List[UnbondingDelegationEntry]

    @classmethod
    def from_proto(cls, proto):
        return cls(
            delegator_address=proto.delegator_address,
            validator_address=proto.validator_address,
            entries=[UnbondingDelegationEntry.from_proto(entry) for entry in proto.entries],
        )

class RedelegationEntry(BaseModel):
    creation_height: int
    completion_time: datetime
    initial_balance: str
    shares_dst: str
    unbonding_id: int
    unbonding_on_hold_ref_count: int

    @classmethod
    def from_proto(cls, proto):
        return cls(
            creation_height=proto.creation_height,
            completion_time=proto.completion_time.ToDatetime(),
            initial_balance=proto.initial_balance,
            shares_dst=proto.shares_dst,
            unbonding_id=proto.unbonding_id,
            unbonding_on_hold_ref_count=proto.unbonding_on_hold_ref_count,
        )

class Redelegation(BaseModel):
    delegator_address: str
    validator_src_address: str
    validator_dst_address: str
    entries: List[RedelegationEntry]

    @classmethod
    def from_proto(cls, proto):
        return cls(
            delegator_address=proto.delegator_address,
            validator_src_address=proto.validator_src_address,
            validator_dst_address=proto.validator_dst_address,
            entries=[RedelegationEntry.from_proto(entry) for entry in proto.entries],
        )

class Params(BaseModel):
    unbonding_time: timedelta
    max_validators: int
    max_entries: int
    historical_entries: int
    bond_denom: str
    min_commission_rate: str

    @classmethod
    def from_proto(cls, proto):
        return cls(
            unbonding_time=proto.unbonding_time.ToTimedelta(),
            max_validators=proto.max_validators,
            max_entries=proto.max_entries,
            historical_entries=proto.historical_entries,
            bond_denom=proto.bond_denom,
            min_commission_rate=proto.min_commission_rate,
        )

class DelegationResponse(BaseModel):
    delegation: Delegation
    balance: dict  # Assuming Coin is a dictionary

    @classmethod
    def from_proto(cls, proto):
        return cls(
            delegation=Delegation.from_proto(proto.delegation),
            balance=dict(proto.balance),  # Convert to dict as needed
        )

class RedelegationEntryResponse(BaseModel):
    redelegation_entry: RedelegationEntry
    balance: str

    @classmethod
    def from_proto(cls, proto):
        return cls(
            redelegation_entry=RedelegationEntry.from_proto(proto.redelegation_entry),
            balance=proto.balance,
        )

class RedelegationResponse(BaseModel):
    redelegation: Redelegation
    entries: List[RedelegationEntryResponse]

    @classmethod
    def from_proto(cls, proto):
        return cls(
            redelegation=Redelegation.from_proto(proto.redelegation),
            entries=[RedelegationEntryResponse.from_proto(entry) for entry in proto.entries],
        )

class Pool(BaseModel):
    not_bonded_tokens: str
    bonded_tokens: str

    @classmethod
    def from_proto(cls, proto):
        return cls(
            not_bonded_tokens=proto.not_bonded_tokens,
            bonded_tokens=proto.bonded_tokens,
        )

class ValidatorUpdates(BaseModel):
    updates: List[dict]  # Assuming ValidatorUpdate is a dictionary

    @classmethod
    def from_proto(cls, proto):
        return cls(
            updates=[dict(update) for update in proto.updates],  # Convert to dict as needed
        )
