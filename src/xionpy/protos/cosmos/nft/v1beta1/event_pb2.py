# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/nft/v1beta1/event.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'cosmos/nft/v1beta1/event.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63osmos/nft/v1beta1/event.proto\x12\x12\x63osmos.nft.v1beta1\"j\n\tEventSend\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x16\n\x06sender\x18\x03 \x01(\tR\x06sender\x12\x1a\n\x08receiver\x18\x04 \x01(\tR\x08receiver\"L\n\tEventMint\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x14\n\x05owner\x18\x03 \x01(\tR\x05owner\"L\n\tEventBurn\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x14\n\x05owner\x18\x03 \x01(\tR\x05ownerB\xa2\x01\n\x16\x63om.cosmos.nft.v1beta1B\nEventProtoP\x01Z\x12\x63osmossdk.io/x/nft\xa2\x02\x03\x43NX\xaa\x02\x12\x43osmos.Nft.V1beta1\xca\x02\x12\x43osmos\\Nft\\V1beta1\xe2\x02\x1e\x43osmos\\Nft\\V1beta1\\GPBMetadata\xea\x02\x14\x43osmos::Nft::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.nft.v1beta1.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.cosmos.nft.v1beta1B\nEventProtoP\001Z\022cosmossdk.io/x/nft\242\002\003CNX\252\002\022Cosmos.Nft.V1beta1\312\002\022Cosmos\\Nft\\V1beta1\342\002\036Cosmos\\Nft\\V1beta1\\GPBMetadata\352\002\024Cosmos::Nft::V1beta1'
  _globals['_EVENTSEND']._serialized_start=54
  _globals['_EVENTSEND']._serialized_end=160
  _globals['_EVENTMINT']._serialized_start=162
  _globals['_EVENTMINT']._serialized_end=238
  _globals['_EVENTBURN']._serialized_start=240
  _globals['_EVENTBURN']._serialized_end=316
# @@protoc_insertion_point(module_scope)
