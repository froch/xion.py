# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xion/jwk/v1/tx.proto
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
    'xion/jwk/v1/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xion.jwk.v1 import audience_pb2 as xion_dot_jwk_dot_v1_dot_audience__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14xion/jwk/v1/tx.proto\x12\x0bxion.jwk.v1\x1a\x1axion/jwk/v1/audience.proto\"I\n\x16MsgCreateAudienceClaim\x12\x14\n\x05\x61\x64min\x18\x01 \x01(\tR\x05\x61\x64min\x12\x19\n\x08\x61ud_hash\x18\x02 \x01(\x0cR\x07\x61udHash\" \n\x1eMsgCreateAudienceClaimResponse\"I\n\x16MsgDeleteAudienceClaim\x12\x14\n\x05\x61\x64min\x18\x01 \x01(\tR\x05\x61\x64min\x12\x19\n\x08\x61ud_hash\x18\x02 \x01(\x0cR\x07\x61udHash\" \n\x1eMsgDeleteAudienceClaimResponse\"M\n\x11MsgCreateAudience\x12\x14\n\x05\x61\x64min\x18\x01 \x01(\tR\x05\x61\x64min\x12\x10\n\x03\x61ud\x18\x02 \x01(\tR\x03\x61ud\x12\x10\n\x03key\x18\x03 \x01(\tR\x03key\"N\n\x19MsgCreateAudienceResponse\x12\x31\n\x08\x61udience\x18\x01 \x01(\x0b\x32\x15.xion.jwk.v1.AudienceR\x08\x61udience\"j\n\x11MsgUpdateAudience\x12\x14\n\x05\x61\x64min\x18\x01 \x01(\tR\x05\x61\x64min\x12\x1b\n\tnew_admin\x18\x02 \x01(\tR\x08newAdmin\x12\x10\n\x03\x61ud\x18\x03 \x01(\tR\x03\x61ud\x12\x10\n\x03key\x18\x04 \x01(\tR\x03key\"N\n\x19MsgUpdateAudienceResponse\x12\x31\n\x08\x61udience\x18\x01 \x01(\x0b\x32\x15.xion.jwk.v1.AudienceR\x08\x61udience\";\n\x11MsgDeleteAudience\x12\x14\n\x05\x61\x64min\x18\x01 \x01(\tR\x05\x61\x64min\x12\x10\n\x03\x61ud\x18\x02 \x01(\tR\x03\x61ud\"\x1b\n\x19MsgDeleteAudienceResponse2\xe5\x03\n\x03Msg\x12g\n\x13\x43reateAudienceClaim\x12#.xion.jwk.v1.MsgCreateAudienceClaim\x1a+.xion.jwk.v1.MsgCreateAudienceClaimResponse\x12g\n\x13\x44\x65leteAudienceClaim\x12#.xion.jwk.v1.MsgDeleteAudienceClaim\x1a+.xion.jwk.v1.MsgDeleteAudienceClaimResponse\x12X\n\x0e\x43reateAudience\x12\x1e.xion.jwk.v1.MsgCreateAudience\x1a&.xion.jwk.v1.MsgCreateAudienceResponse\x12X\n\x0eUpdateAudience\x12\x1e.xion.jwk.v1.MsgUpdateAudience\x1a&.xion.jwk.v1.MsgUpdateAudienceResponse\x12X\n\x0e\x44\x65leteAudience\x12\x1e.xion.jwk.v1.MsgDeleteAudience\x1a&.xion.jwk.v1.MsgDeleteAudienceResponseB\x90\x01\n\x0f\x63om.xion.jwk.v1B\x07TxProtoP\x01Z&github.com/burnt-labs/xion/x/jwk/types\xa2\x02\x03XJX\xaa\x02\x0bXion.Jwk.V1\xca\x02\x0bXion\\Jwk\\V1\xe2\x02\x17Xion\\Jwk\\V1\\GPBMetadata\xea\x02\rXion::Jwk::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xion.jwk.v1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.xion.jwk.v1B\007TxProtoP\001Z&github.com/burnt-labs/xion/x/jwk/types\242\002\003XJX\252\002\013Xion.Jwk.V1\312\002\013Xion\\Jwk\\V1\342\002\027Xion\\Jwk\\V1\\GPBMetadata\352\002\rXion::Jwk::V1'
  _globals['_MSGCREATEAUDIENCECLAIM']._serialized_start=65
  _globals['_MSGCREATEAUDIENCECLAIM']._serialized_end=138
  _globals['_MSGCREATEAUDIENCECLAIMRESPONSE']._serialized_start=140
  _globals['_MSGCREATEAUDIENCECLAIMRESPONSE']._serialized_end=172
  _globals['_MSGDELETEAUDIENCECLAIM']._serialized_start=174
  _globals['_MSGDELETEAUDIENCECLAIM']._serialized_end=247
  _globals['_MSGDELETEAUDIENCECLAIMRESPONSE']._serialized_start=249
  _globals['_MSGDELETEAUDIENCECLAIMRESPONSE']._serialized_end=281
  _globals['_MSGCREATEAUDIENCE']._serialized_start=283
  _globals['_MSGCREATEAUDIENCE']._serialized_end=360
  _globals['_MSGCREATEAUDIENCERESPONSE']._serialized_start=362
  _globals['_MSGCREATEAUDIENCERESPONSE']._serialized_end=440
  _globals['_MSGUPDATEAUDIENCE']._serialized_start=442
  _globals['_MSGUPDATEAUDIENCE']._serialized_end=548
  _globals['_MSGUPDATEAUDIENCERESPONSE']._serialized_start=550
  _globals['_MSGUPDATEAUDIENCERESPONSE']._serialized_end=628
  _globals['_MSGDELETEAUDIENCE']._serialized_start=630
  _globals['_MSGDELETEAUDIENCE']._serialized_end=689
  _globals['_MSGDELETEAUDIENCERESPONSE']._serialized_start=691
  _globals['_MSGDELETEAUDIENCERESPONSE']._serialized_end=718
  _globals['_MSG']._serialized_start=721
  _globals['_MSG']._serialized_end=1206
# @@protoc_insertion_point(module_scope)
