from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, List

from google.protobuf.internal.well_known_types import Timestamp
from pydantic import BaseModel

from xionpy.services.base.model import Coin


@dataclass
class ProposalStatus(Enum):
    UNSPECIFIED = "PROPOSAL_STATUS_UNSPECIFIED"
    DEPOSIT_PERIOD = "PROPOSAL_STATUS_DEPOSIT_PERIOD"
    VOTING_PERIOD = "PROPOSAL_STATUS_VOTING_PERIOD"
    PASSED = "PROPOSAL_STATUS_PASSED"
    REJECTED = "PROPOSAL_STATUS_REJECTED"
    FAILED = "PROPOSAL_STATUS_FAILED"

    @classmethod
    def from_proto(cls, value: int) -> "ValidatorStatus":
        if value == 0:
            return cls.UNSPECIFIED
        if value == 1:
            return cls.DEPOSIT_PERIOD
        if value == 2:
            return cls.VOTING_PERIOD
        if value == 3:
            return cls.PASSED
        if value == 4:
            return cls.REJECTED
        if value == 5:
            return cls.FAILED
        raise RuntimeError(f"Unable to decode proposal status: {value}")

class TallyResult(BaseModel):
    yes_count: str
    abstain_count: str
    no_count: str
    no_with_veto_count: str

    @classmethod
    def from_proto(cls, tally_result):
        return cls(
            yes_count=tally_result.yes_count,
            abstain_count=tally_result.abstain_count,
            no_count=tally_result.no_count,
            no_with_veto_count=tally_result.no_with_veto_count,
        )

class Proposal(BaseModel):
    id: int
    messages: List[Any]
    status: ProposalStatus
    final_tally_result: TallyResult
    submit_time: datetime
    deposit_end_time: datetime
    total_deposit: List[Coin]
    voting_start_time: datetime
    voting_end_time: datetime
    metadata: str
    title: str
    summary: str
    proposer: str
    expedited: bool
    failed_reason: str

    @classmethod
    def from_proto(cls, proposal):
        return cls(
            id=proposal.id,
            messages=proposal.messages,
            status=ProposalStatus.from_proto(proposal.status),
            final_tally_result=TallyResult.from_proto(proposal.final_tally_result),
            submit_time=Timestamp.ToDatetime(proposal.submit_time),
            deposit_end_time=Timestamp.ToDatetime(proposal.deposit_end_time),
            total_deposit=[Coin.from_proto(coin) for coin in proposal.total_deposit],
            voting_start_time=Timestamp.ToDatetime(proposal.voting_start_time),
            voting_end_time=Timestamp.ToDatetime(proposal.voting_end_time),
            metadata=proposal.metadata,
            title=proposal.title,
            summary=proposal.summary,
            proposer=proposal.proposer,
            expedited=proposal.expedited,
            failed_reason=proposal.failed_reason,
        )
