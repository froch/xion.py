from typing import Optional, List

from pydantic import BaseModel


class ConsensusModel(BaseModel):
    block: Optional[int]
    app: Optional[int] = None


class PartSetHeaderModel(BaseModel):
    total: Optional[int]
    hash: Optional[str]


class BlockIDModel(BaseModel):
    hash: Optional[str]
    part_set_header: Optional[PartSetHeaderModel]


class EvidenceListModel(BaseModel):
    evidence: Optional[List[str]]


class CommitModel(BaseModel):
    height: Optional[int]
    round: Optional[int]
    block_id: Optional[BlockIDModel]
    signatures: Optional[List[str]]


class HeaderModel(BaseModel):
    version: Optional[ConsensusModel]
    chain_id: Optional[str]
    height: Optional[int]
    time: Optional[str]  # Can be more specific like `datetime` or `Timestamp` depending on your usage
    last_block_id: Optional[BlockIDModel]
    last_commit_hash: Optional[str]
    data_hash: Optional[str]
    validators_hash: Optional[str]
    next_validators_hash: Optional[str]
    consensus_hash: Optional[str]
    app_hash: Optional[str]
    last_results_hash: Optional[str]
    evidence_hash: Optional[str]
    proposer_address: Optional[str]


class BlockModel(BaseModel):
    header: Optional[HeaderModel]
    data: Optional[str]  # Assuming this is a base64 encoded string or similar.
    evidence: Optional[EvidenceListModel]
    last_commit: Optional[CommitModel]
