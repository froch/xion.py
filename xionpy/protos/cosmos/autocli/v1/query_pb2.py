# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/autocli/v1/query.proto
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
    'cosmos/autocli/v1/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.autocli.v1 import options_pb2 as cosmos_dot_autocli_dot_v1_dot_options__pb2
from cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63osmos/autocli/v1/query.proto\x12\x11\x63osmos.autocli.v1\x1a\x1f\x63osmos/autocli/v1/options.proto\x1a\x1b\x63osmos/query/v1/query.proto\"\x13\n\x11\x41ppOptionsRequest\"\xd9\x01\n\x12\x41ppOptionsResponse\x12_\n\x0emodule_options\x18\x01 \x03(\x0b\x32\x38.cosmos.autocli.v1.AppOptionsResponse.ModuleOptionsEntryR\rmoduleOptions\x1a\x62\n\x12ModuleOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32 .cosmos.autocli.v1.ModuleOptionsR\x05value:\x02\x38\x01\x32i\n\x05Query\x12`\n\nAppOptions\x12$.cosmos.autocli.v1.AppOptionsRequest\x1a%.cosmos.autocli.v1.AppOptionsResponse\"\x05\x88\xe7\xb0*\x00\x42\xb4\x01\n\x15\x63om.cosmos.autocli.v1B\nQueryProtoP\x01Z)cosmossdk.io/api/cosmos/base/cli/v1;cliv1\xa2\x02\x03\x43\x41X\xaa\x02\x11\x43osmos.Autocli.V1\xca\x02\x11\x43osmos\\Autocli\\V1\xe2\x02\x1d\x43osmos\\Autocli\\V1\\GPBMetadata\xea\x02\x13\x43osmos::Autocli::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.autocli.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.cosmos.autocli.v1B\nQueryProtoP\001Z)cosmossdk.io/api/cosmos/base/cli/v1;cliv1\242\002\003CAX\252\002\021Cosmos.Autocli.V1\312\002\021Cosmos\\Autocli\\V1\342\002\035Cosmos\\Autocli\\V1\\GPBMetadata\352\002\023Cosmos::Autocli::V1'
  _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._loaded_options = None
  _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_QUERY'].methods_by_name['AppOptions']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AppOptions']._serialized_options = b'\210\347\260*\000'
  _globals['_APPOPTIONSREQUEST']._serialized_start=114
  _globals['_APPOPTIONSREQUEST']._serialized_end=133
  _globals['_APPOPTIONSRESPONSE']._serialized_start=136
  _globals['_APPOPTIONSRESPONSE']._serialized_end=353
  _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._serialized_start=255
  _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._serialized_end=353
  _globals['_QUERY']._serialized_start=355
  _globals['_QUERY']._serialized_end=460
# @@protoc_insertion_point(module_scope)
