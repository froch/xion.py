from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class SignedMsgTypeEnum(Enum):
    UNKNOWN = "SIGNED_MSG_TYPE_UNKNOWN"
    PREVOTE = "SIGNED_MSG_TYPE_PREVOTE"
    PRECOMMIT = "SIGNED_MSG_TYPE_PRECOMMIT"
    PROPOSAL = "SIGNED_MSG_TYPE_PROPOSAL"

    @classmethod
    def from_proto(cls, value: str) -> "SignedMsgTypeEnum":
        for t in cls:
            if t.value == value:
                return t
        raise ValueError(f"Invalid SIGNED_MSG_TYPE: {value}")


class PageRequestModel(BaseModel):
    key: Optional[bytes]
    offset: Optional[int]
    limit: Optional[int]
    count_total: Optional[bool]
    reverse: Optional[bool]


class PageResponseModel(BaseModel):
    next_key: Optional[bytes] = None
    total: Optional[int] = None


class ConsensusModel(BaseModel):
    block: Optional[int]
    app: Optional[int] = None


class PartSetHeaderModel(BaseModel):
    total: Optional[int]
    hash: Optional[str]


class BlockIDModel(BaseModel):
    hash: Optional[str]
    part_set_header: Optional[PartSetHeaderModel]


class HeaderModel(BaseModel):
    version: Optional[ConsensusModel]
    chain_id: Optional[str]
    height: Optional[int]
    time: Optional[datetime]
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


class PublicKeyModel(BaseModel):
    ed25519: Optional[str] = None
    secp256k1: Optional[str] = None


class ValidatorModel(BaseModel):
    address: Optional[str]
    pub_key: Optional[PublicKeyModel]
    voting_power: Optional[int]
    proposer_priority: Optional[int]


class CommitSigModel(BaseModel):
    block_id_flag: Optional[str]
    validator_address: Optional[str]
    timestamp: datetime
    signature: Optional[str]


class CommitModel(BaseModel):
    height: Optional[int]
    round: Optional[int] = None
    block_id: Optional[BlockIDModel]
    signatures: Optional[List[CommitSigModel]]


class SignedHeaderModel(BaseModel):
    header: Optional[HeaderModel]
    commit: Optional[CommitModel]


class ValidatorSetModel(BaseModel):
    validators: Optional[List[ValidatorModel]]
    proposer: Optional[ValidatorModel]
    total_voting_power: Optional[int]


class LightBlockModel(BaseModel):
    signed_header: Optional[SignedHeaderModel]
    validator_set: Optional[ValidatorSetModel]


class LightClientAttackEvidenceModel(BaseModel):
    conflicting_block: Optional[LightBlockModel]
    common_height: Optional[int]
    byzantine_validators: Optional[List[ValidatorModel]]
    total_voting_power: Optional[int]
    timestamp: Optional[datetime]


class VoteModel(BaseModel):
    type: Optional[SignedMsgTypeEnum]
    height: Optional[int]
    round: Optional[int]
    block_id: Optional[BlockIDModel]
    timestamp: Optional[datetime]
    validator_address: Optional[str]
    validator_index: Optional[int]
    signature: Optional[str]
    extension: Optional[str]
    extension_signature: Optional[str]


class DuplicateVoteEvidenceModel(BaseModel):
    vote_a: Optional[VoteModel]
    vote_b: Optional[VoteModel]
    total_voting_power: Optional[int]
    validator_power: Optional[int]
    timestamp: Optional[datetime]


class EvidenceModel(BaseModel):
    duplicate_vote_evidence: Optional[DuplicateVoteEvidenceModel]
    light_client_attack_evidence: Optional[LightClientAttackEvidenceModel]


class EvidenceListModel(BaseModel):
    evidence: Optional[List[EvidenceModel]] = {}


class DataModel(BaseModel):
    txs: Optional[List[str]] = []


class BlockModel(BaseModel):
    header: Optional[HeaderModel]
    data: Optional[DataModel]
    evidence: Optional[EvidenceListModel]
    last_commit: Optional[CommitModel]


class ModuleModel(BaseModel):
    path: Optional[str]
    version: Optional[str]
    sum: Optional[str] = None


class VersionInfoModel(BaseModel):
    name: Optional[str]
    app_name: Optional[str]
    version: Optional[str]
    git_commit: Optional[str]
    build_tags: Optional[str]
    go_version: Optional[str]
    build_deps: Optional[List[ModuleModel]]
    cosmos_sdk_version: Optional[str]


class ProofOpModel(BaseModel):
    type: Optional[str]
    key: Optional[str]
    data: Optional[str]


class ProofOpsModel(BaseModel):
    ops: Optional[List[ProofOpModel]]


class ABCIQueryRequestModel(BaseModel):
    data: Optional[str]
    path: Optional[str]
    height: Optional[int]
    prove: Optional[bool]


class ABCIQueryResponseModel(BaseModel):
    code: Optional[int]
    log: Optional[str]
    info: Optional[str]
    index: Optional[int]
    key: Optional[str]
    value: Optional[str]
    proof_ops: Optional[ProofOpsModel]
    height: Optional[int]
    codespace: Optional[str]


class GetValidatorSetByHeightRequestModel(BaseModel):
    height: Optional[int]
    pagination: Optional[PageRequestModel]


class GetValidatorSetByHeightResponseModel(BaseModel):
    block_height: Optional[int]
    validators: Optional[List[ValidatorModel]]
    pagination: Optional[PageResponseModel]


class GetLatestValidatorSetRequestModel(BaseModel):
    pagination: Optional[PageRequestModel]


class GetLatestValidatorSetResponseModel(BaseModel):
    block_height: Optional[int]
    validators: Optional[List[ValidatorModel]]
    pagination: Optional[PageResponseModel]


class GetBlockByHeightRequestModel(BaseModel):
    height: Optional[int]


class GetBlockByHeightResponseModel(BaseModel):
    block_id: Optional[BlockIDModel]
    block: Optional[BlockModel]
    sdk_block: Optional[BlockModel]


class GetLatestBlockRequestModel(BaseModel):
    pass


class GetLatestBlockResponseModel(BaseModel):
    block_id: Optional[BlockIDModel]
    block: Optional[BlockModel]
    sdk_block: Optional[BlockModel]


class GetSyncingRequestModel(BaseModel):
    pass


class GetSyncingResponseModel(BaseModel):
    syncing: Optional[bool] = False


class GetNodeInfoRequestModel(BaseModel):
    pass


class ProtocolVersionModel(BaseModel):
    p2p: Optional[int]
    block: Optional[int]
    app: Optional[int] = None


class DefaultNodeInfoOtherModel(BaseModel):
    tx_index: Optional[str]
    rpc_address: Optional[str]


class DefaultNodeInfoModel(BaseModel):
    protocol_version: Optional[ProtocolVersionModel]
    default_node_id: Optional[str]
    listen_addr: Optional[str]
    network: Optional[str]
    version: Optional[str]
    channels: Optional[str]
    moniker: Optional[str]
    other: Optional[DefaultNodeInfoOtherModel]


class GetNodeInfoResponseModel(BaseModel):
    default_node_info: Optional[DefaultNodeInfoModel]
    application_version: Optional[VersionInfoModel]


class NetAddressModel(BaseModel):
    id: Optional[str]
    ip: Optional[str]
    port: Optional[int]
