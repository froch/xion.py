# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xion/mint/v1/mint.proto
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
    'xion/mint/v1/mint.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17xion/mint/v1/mint.proto\x12\x0cxion.mint.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xcf\x01\n\x06Minter\x12Z\n\tinflation\x18\x01 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\tinflation\x12i\n\x11\x61nnual_provisions\x18\x02 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x10\x61nnualProvisions\"\x83\x04\n\x06Params\x12\x1d\n\nmint_denom\x18\x01 \x01(\tR\tmintDenom\x12p\n\x15inflation_rate_change\x18\x02 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x13inflationRateChange\x12\x61\n\rinflation_max\x18\x03 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0cinflationMax\x12\x61\n\rinflation_min\x18\x04 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0cinflationMin\x12]\n\x0bgoal_bonded\x18\x05 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\ngoalBonded\x12&\n\x0f\x62locks_per_year\x18\x06 \x01(\x04R\rblocksPerYear:\x1b\x98\xa0\x1f\x00\x8a\xe7\xb0*\x12xion/x/mint/ParamsB\x98\x01\n\x10\x63om.xion.mint.v1B\tMintProtoP\x01Z\'github.com/burnt-labs/xion/x/mint/types\xa2\x02\x03XMX\xaa\x02\x0cXion.Mint.V1\xca\x02\x0cXion\\Mint\\V1\xe2\x02\x18Xion\\Mint\\V1\\GPBMetadata\xea\x02\x0eXion::Mint::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xion.mint.v1.mint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.xion.mint.v1B\tMintProtoP\001Z\'github.com/burnt-labs/xion/x/mint/types\242\002\003XMX\252\002\014Xion.Mint.V1\312\002\014Xion\\Mint\\V1\342\002\030Xion\\Mint\\V1\\GPBMetadata\352\002\016Xion::Mint::V1'
  _globals['_MINTER'].fields_by_name['inflation']._loaded_options = None
  _globals['_MINTER'].fields_by_name['inflation']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _globals['_MINTER'].fields_by_name['annual_provisions']._loaded_options = None
  _globals['_MINTER'].fields_by_name['annual_provisions']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _globals['_PARAMS'].fields_by_name['inflation_rate_change']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['inflation_rate_change']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _globals['_PARAMS'].fields_by_name['inflation_max']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['inflation_max']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _globals['_PARAMS'].fields_by_name['inflation_min']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['inflation_min']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _globals['_PARAMS'].fields_by_name['goal_bonded']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['goal_bonded']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\230\240\037\000\212\347\260*\022xion/x/mint/Params'
  _globals['_MINTER']._serialized_start=110
  _globals['_MINTER']._serialized_end=317
  _globals['_PARAMS']._serialized_start=320
  _globals['_PARAMS']._serialized_end=835
# @@protoc_insertion_point(module_scope)
