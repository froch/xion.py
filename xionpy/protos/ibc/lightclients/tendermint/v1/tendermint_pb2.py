# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ibc/lightclients/tendermint/v1/tendermint.proto
# Protobuf Python Version: 5.28.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    0,
    '',
    'ibc/lightclients/tendermint/v1/tendermint.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tendermint.types import validator_pb2 as tendermint_dot_types_dot_validator__pb2
from tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from cosmos.ics23.v1 import proofs_pb2 as cosmos_dot_ics23_dot_v1_dot_proofs__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from ibc.core.commitment.v1 import commitment_pb2 as ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/ibc/lightclients/tendermint/v1/tendermint.proto\x12\x1eibc.lightclients.tendermint.v1\x1a tendermint/types/validator.proto\x1a\x1ctendermint/types/types.proto\x1a\x1c\x63osmos/ics23/v1/proofs.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/commitment/v1/commitment.proto\x1a\x14gogoproto/gogo.proto\"\xe2\x05\n\x0b\x43lientState\x12\x19\n\x08\x63hain_id\x18\x01 \x01(\tR\x07\x63hainId\x12O\n\x0btrust_level\x18\x02 \x01(\x0b\x32(.ibc.lightclients.tendermint.v1.FractionB\x04\xc8\xde\x1f\x00R\ntrustLevel\x12L\n\x0ftrusting_period\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01R\x0etrustingPeriod\x12N\n\x10unbonding_period\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01R\x0funbondingPeriod\x12K\n\x0fmax_clock_drift\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01R\rmaxClockDrift\x12\x45\n\rfrozen_height\x18\x06 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0c\x66rozenHeight\x12\x45\n\rlatest_height\x18\x07 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0clatestHeight\x12;\n\x0bproof_specs\x18\x08 \x03(\x0b\x32\x1a.cosmos.ics23.v1.ProofSpecR\nproofSpecs\x12!\n\x0cupgrade_path\x18\t \x03(\tR\x0bupgradePath\x12=\n\x19\x61llow_update_after_expiry\x18\n \x01(\x08\x42\x02\x18\x01R\x16\x61llowUpdateAfterExpiry\x12I\n\x1f\x61llow_update_after_misbehaviour\x18\x0b \x01(\x08\x42\x02\x18\x01R\x1c\x61llowUpdateAfterMisbehaviour:\x04\x88\xa0\x1f\x00\"\x80\x02\n\x0e\x43onsensusState\x12\x42\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\ttimestamp\x12<\n\x04root\x18\x02 \x01(\x0b\x32\".ibc.core.commitment.v1.MerkleRootB\x04\xc8\xde\x1f\x00R\x04root\x12\x66\n\x14next_validators_hash\x18\x03 \x01(\x0c\x42\x34\xfa\xde\x1f\x30github.com/cometbft/cometbft/libs/bytes.HexBytesR\x12nextValidatorsHash:\x04\x88\xa0\x1f\x00\"\xd5\x01\n\x0cMisbehaviour\x12\x1f\n\tclient_id\x18\x01 \x01(\tB\x02\x18\x01R\x08\x63lientId\x12N\n\x08header_1\x18\x02 \x01(\x0b\x32&.ibc.lightclients.tendermint.v1.HeaderB\x0b\xe2\xde\x1f\x07Header1R\x07header1\x12N\n\x08header_2\x18\x03 \x01(\x0b\x32&.ibc.lightclients.tendermint.v1.HeaderB\x0b\xe2\xde\x1f\x07Header2R\x07header2:\x04\x88\xa0\x1f\x00\"\xb0\x02\n\x06Header\x12I\n\rsigned_header\x18\x01 \x01(\x0b\x32\x1e.tendermint.types.SignedHeaderB\x04\xd0\xde\x1f\x01R\x0csignedHeader\x12\x43\n\rvalidator_set\x18\x02 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSetR\x0cvalidatorSet\x12G\n\x0etrusted_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\rtrustedHeight\x12M\n\x12trusted_validators\x18\x04 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSetR\x11trustedValidators\"J\n\x08\x46raction\x12\x1c\n\tnumerator\x18\x01 \x01(\x04R\tnumerator\x12 \n\x0b\x64\x65nominator\x18\x02 \x01(\x04R\x0b\x64\x65nominatorB\x9c\x02\n\"com.ibc.lightclients.tendermint.v1B\x0fTendermintProtoP\x01ZJgithub.com/cosmos/ibc-go/v8/modules/light-clients/07-tendermint;tendermint\xa2\x02\x03ILT\xaa\x02\x1eIbc.Lightclients.Tendermint.V1\xca\x02\x1eIbc\\Lightclients\\Tendermint\\V1\xe2\x02*Ibc\\Lightclients\\Tendermint\\V1\\GPBMetadata\xea\x02!Ibc::Lightclients::Tendermint::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.tendermint.v1.tendermint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.ibc.lightclients.tendermint.v1B\017TendermintProtoP\001ZJgithub.com/cosmos/ibc-go/v8/modules/light-clients/07-tendermint;tendermint\242\002\003ILT\252\002\036Ibc.Lightclients.Tendermint.V1\312\002\036Ibc\\Lightclients\\Tendermint\\V1\342\002*Ibc\\Lightclients\\Tendermint\\V1\\GPBMetadata\352\002!Ibc::Lightclients::Tendermint::V1'
  _globals['_CLIENTSTATE'].fields_by_name['trust_level']._loaded_options = None
  _globals['_CLIENTSTATE'].fields_by_name['trust_level']._serialized_options = b'\310\336\037\000'
  _globals['_CLIENTSTATE'].fields_by_name['trusting_period']._loaded_options = None
  _globals['_CLIENTSTATE'].fields_by_name['trusting_period']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _globals['_CLIENTSTATE'].fields_by_name['unbonding_period']._loaded_options = None
  _globals['_CLIENTSTATE'].fields_by_name['unbonding_period']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _globals['_CLIENTSTATE'].fields_by_name['max_clock_drift']._loaded_options = None
  _globals['_CLIENTSTATE'].fields_by_name['max_clock_drift']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _globals['_CLIENTSTATE'].fields_by_name['frozen_height']._loaded_options = None
  _globals['_CLIENTSTATE'].fields_by_name['frozen_height']._serialized_options = b'\310\336\037\000'
  _globals['_CLIENTSTATE'].fields_by_name['latest_height']._loaded_options = None
  _globals['_CLIENTSTATE'].fields_by_name['latest_height']._serialized_options = b'\310\336\037\000'
  _globals['_CLIENTSTATE'].fields_by_name['allow_update_after_expiry']._loaded_options = None
  _globals['_CLIENTSTATE'].fields_by_name['allow_update_after_expiry']._serialized_options = b'\030\001'
  _globals['_CLIENTSTATE'].fields_by_name['allow_update_after_misbehaviour']._loaded_options = None
  _globals['_CLIENTSTATE'].fields_by_name['allow_update_after_misbehaviour']._serialized_options = b'\030\001'
  _globals['_CLIENTSTATE']._loaded_options = None
  _globals['_CLIENTSTATE']._serialized_options = b'\210\240\037\000'
  _globals['_CONSENSUSSTATE'].fields_by_name['timestamp']._loaded_options = None
  _globals['_CONSENSUSSTATE'].fields_by_name['timestamp']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_CONSENSUSSTATE'].fields_by_name['root']._loaded_options = None
  _globals['_CONSENSUSSTATE'].fields_by_name['root']._serialized_options = b'\310\336\037\000'
  _globals['_CONSENSUSSTATE'].fields_by_name['next_validators_hash']._loaded_options = None
  _globals['_CONSENSUSSTATE'].fields_by_name['next_validators_hash']._serialized_options = b'\372\336\0370github.com/cometbft/cometbft/libs/bytes.HexBytes'
  _globals['_CONSENSUSSTATE']._loaded_options = None
  _globals['_CONSENSUSSTATE']._serialized_options = b'\210\240\037\000'
  _globals['_MISBEHAVIOUR'].fields_by_name['client_id']._loaded_options = None
  _globals['_MISBEHAVIOUR'].fields_by_name['client_id']._serialized_options = b'\030\001'
  _globals['_MISBEHAVIOUR'].fields_by_name['header_1']._loaded_options = None
  _globals['_MISBEHAVIOUR'].fields_by_name['header_1']._serialized_options = b'\342\336\037\007Header1'
  _globals['_MISBEHAVIOUR'].fields_by_name['header_2']._loaded_options = None
  _globals['_MISBEHAVIOUR'].fields_by_name['header_2']._serialized_options = b'\342\336\037\007Header2'
  _globals['_MISBEHAVIOUR']._loaded_options = None
  _globals['_MISBEHAVIOUR']._serialized_options = b'\210\240\037\000'
  _globals['_HEADER'].fields_by_name['signed_header']._loaded_options = None
  _globals['_HEADER'].fields_by_name['signed_header']._serialized_options = b'\320\336\037\001'
  _globals['_HEADER'].fields_by_name['trusted_height']._loaded_options = None
  _globals['_HEADER'].fields_by_name['trusted_height']._serialized_options = b'\310\336\037\000'
  _globals['_CLIENTSTATE']._serialized_start=339
  _globals['_CLIENTSTATE']._serialized_end=1077
  _globals['_CONSENSUSSTATE']._serialized_start=1080
  _globals['_CONSENSUSSTATE']._serialized_end=1336
  _globals['_MISBEHAVIOUR']._serialized_start=1339
  _globals['_MISBEHAVIOUR']._serialized_end=1552
  _globals['_HEADER']._serialized_start=1555
  _globals['_HEADER']._serialized_end=1859
  _globals['_FRACTION']._serialized_start=1861
  _globals['_FRACTION']._serialized_end=1935
# @@protoc_insertion_point(module_scope)
