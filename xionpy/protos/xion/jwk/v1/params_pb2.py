# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xion/jwk/v1/params.proto
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
    'xion/jwk/v1/params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18xion/jwk/v1/params.proto\x12\x0bxion.jwk.v1\x1a\x14gogoproto/gogo.proto\"\x83\x01\n\x06Params\x12\x37\n\x0btime_offset\x18\x01 \x01(\x04\x42\x16\xf2\xde\x1f\x12yaml:\"time_offset\"R\ntimeOffset\x12@\n\x0e\x64\x65ployment_gas\x18\x02 \x01(\x04\x42\x19\xf2\xde\x1f\x15yaml:\"deployment_gas\"R\rdeploymentGasB\x94\x01\n\x0f\x63om.xion.jwk.v1B\x0bParamsProtoP\x01Z&github.com/burnt-labs/xion/x/jwk/types\xa2\x02\x03XJX\xaa\x02\x0bXion.Jwk.V1\xca\x02\x0bXion\\Jwk\\V1\xe2\x02\x17Xion\\Jwk\\V1\\GPBMetadata\xea\x02\rXion::Jwk::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xion.jwk.v1.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.xion.jwk.v1B\013ParamsProtoP\001Z&github.com/burnt-labs/xion/x/jwk/types\242\002\003XJX\252\002\013Xion.Jwk.V1\312\002\013Xion\\Jwk\\V1\342\002\027Xion\\Jwk\\V1\\GPBMetadata\352\002\rXion::Jwk::V1'
  _globals['_PARAMS'].fields_by_name['time_offset']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['time_offset']._serialized_options = b'\362\336\037\022yaml:\"time_offset\"'
  _globals['_PARAMS'].fields_by_name['deployment_gas']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['deployment_gas']._serialized_options = b'\362\336\037\025yaml:\"deployment_gas\"'
  _globals['_PARAMS']._serialized_start=64
  _globals['_PARAMS']._serialized_end=195
# @@protoc_insertion_point(module_scope)
