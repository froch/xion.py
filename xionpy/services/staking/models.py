from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional, Union

import tempora
from pydantic import BaseModel, Field, field_validator

from xionpy.services.base.coin.models import CoinModel
from xionpy.services.base.tendermint.models import HeaderModel, PageResponseModel


class BondStatusEnum(Enum):
    UNSPECIFIED = "BOND_STATUS_UNSPECIFIED"
    UNBONDED = "BOND_STATUS_UNBONDED"
    UNBONDING = "BOND_STATUS_UNBONDING"
    BONDED = "BOND_STATUS_BONDED"

    @classmethod
    def from_proto(cls, value: str) -> "BondStatusEnum":
        for status in cls:
            if status.value == value:
                return status
        raise ValueError(f"Invalid BOND_STATUS: {value}")


class InfractionEnum(Enum):
    UNSPECIFIED = "INFRACTION_UNSPECIFIED"
    DOUBLE_SIGN = "INFRACTION_DOUBLE_SIGN"
    DOWNTIME = "INFRACTION_DOWNTIME"

    @classmethod
    def from_proto(cls, value: int) -> "InfractionEnum":
        if value == 0:
            return cls.UNSPECIFIED
        if value == 1:
            return cls.DOUBLE_SIGN
        if value == 2:
            return cls.DOWNTIME
        raise ValueError(f"Invalid INFRACTION: {value}")


class ValidatorDescriptionModel(BaseModel):
    moniker: str
    identity: Optional[str] = None
    website: Optional[str] = None
    security_contact: Optional[str] = None
    details: Optional[str] = None


class CommissionRatesModel(BaseModel):
    rate: str
    max_rate: str
    max_change_rate: str


class CommissionModel(BaseModel):
    commission_rates: CommissionRatesModel
    update_time: datetime

    @field_validator("update_time", mode="before")
    def parse_update_time(cls, v):
        return datetime.fromisoformat(v.rstrip('Z'))

class ValidatorModel(BaseModel):
    operator_address: str
    consensus_pubkey: Union[bytes, dict]
    jailed: Optional[bool] = Field(default=False)
    status: BondStatusEnum
    tokens: str
    delegator_shares: str
    description: ValidatorDescriptionModel
    unbonding_height: Optional[int] = None
    unbonding_time: Optional[datetime] = None
    commission: CommissionModel
    min_self_delegation: str
    unbonding_on_hold_ref_count: Optional[int] = Field(default=0)
    unbonding_ids: Optional[List[int]] = None

    @field_validator("consensus_pubkey", mode="before")
    def parse_consensus_pubkey(cls, v):
        if isinstance(v, dict) and "@type" in v and v["@type"] == "/cosmos.crypto.ed25519.PubKey":
            return v.get("key").encode()
        return v

    @field_validator("status", mode="before")
    def parse_status(cls, v):
        return BondStatusEnum.from_proto(v)

    @field_validator("unbonding_time", mode="before")
    def parse_unbonding_time(cls, v):
        return datetime.fromisoformat(v.rstrip('Z'))


class DelegationModel(BaseModel):
    delegator_address: str
    validator_address: str
    shares: int


class UnbondingDelegationEntryModel(BaseModel):
    creation_height: int
    completion_time: datetime
    initial_balance: str
    balance: str
    unbonding_id: int
    unbonding_on_hold_ref_count: Optional[int] = None


class UnbondingDelegationModel(BaseModel):
    delegator_address: str
    validator_address: str
    entries: List[UnbondingDelegationEntryModel]


class RedelegationEntryModel(BaseModel):
    creation_height: int
    completion_time: datetime
    initial_balance: str
    shares_dst: str
    unbonding_id: int
    unbonding_on_hold_ref_count: int


class RedelegationModel(BaseModel):
    delegator_address: str
    validator_src_address: str
    validator_dst_address: str
    entries: List[RedelegationEntryModel]


class PoolModel(BaseModel):
    not_bonded_tokens: int
    bonded_tokens: int


class ParamsModel(BaseModel):
    unbonding_time: timedelta
    max_validators: int
    max_entries: int
    historical_entries: int
    bond_denom: str
    min_commission_rate: str

    @field_validator("unbonding_time", mode="before")
    def parse_unbonding_time(cls, v):
        return tempora.parse_timedelta(v)


class DelegationResponseModel(BaseModel):
    delegation: DelegationModel
    balance: CoinModel


class RedelegationEntryResponseModel(BaseModel):
    redelegation_entry: RedelegationEntryModel
    balance: str


class RedelegationResponseModel(BaseModel):
    redelegation: RedelegationModel
    entries: List[RedelegationEntryResponseModel]


class QueryValidatorsResponseModel(BaseModel):
    validators: List[ValidatorModel]


class QueryValidatorResponseModel(BaseModel):
    validator: ValidatorModel


class QueryDelegationResponseModel(BaseModel):
    delegation_response: DelegationResponseModel


class QueryUnbondingDelegationResponseModel(BaseModel):
    unbond: UnbondingDelegationModel


class QueryDelegatorDelegationsResponseModel(BaseModel):
    delegation_responses: List[DelegationResponseModel]


class QueryDelegatorUnbondingDelegationsResponseModel(BaseModel):
    unbonding_responses: List[UnbondingDelegationModel]


class QueryRedelegationsResponseModel(BaseModel):
    redelegation_responses: List[RedelegationResponseModel]


class QueryHistoricalInfoResponseModel(BaseModel):
    header: HeaderModel
    valset: List[ValidatorModel]


class QueryPoolResponseModel(BaseModel):
    pool: PoolModel


class QueryParamsResponseModel(BaseModel):
    params: ParamsModel


class QueryValidatorDelegationsResponseModel(BaseModel):
    delegation_responses: List[DelegationResponseModel]
    pagination: Optional[PageResponseModel]


class QueryValidatorUnbondingDelegationsResponseModel(BaseModel):
    unbonding_responses: List[UnbondingDelegationModel]


class QueryDelegatorValidatorsResponseModel(BaseModel):
    validators: List[ValidatorModel]


class QueryDelegatorValidatorResponseModel(BaseModel):
    validator: ValidatorModel
