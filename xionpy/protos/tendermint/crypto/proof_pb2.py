# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tendermint/crypto/proof.proto
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
    'tendermint/crypto/proof.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtendermint/crypto/proof.proto\x12\x11tendermint.crypto\x1a\x14gogoproto/gogo.proto\"f\n\x05Proof\x12\x14\n\x05total\x18\x01 \x01(\x03R\x05total\x12\x14\n\x05index\x18\x02 \x01(\x03R\x05index\x12\x1b\n\tleaf_hash\x18\x03 \x01(\x0cR\x08leafHash\x12\x14\n\x05\x61unts\x18\x04 \x03(\x0cR\x05\x61unts\"K\n\x07ValueOp\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12.\n\x05proof\x18\x02 \x01(\x0b\x32\x18.tendermint.crypto.ProofR\x05proof\"J\n\x08\x44ominoOp\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05input\x18\x02 \x01(\tR\x05input\x12\x16\n\x06output\x18\x03 \x01(\tR\x06output\"C\n\x07ProofOp\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x10\n\x03key\x18\x02 \x01(\x0cR\x03key\x12\x12\n\x04\x64\x61ta\x18\x03 \x01(\x0cR\x04\x64\x61ta\">\n\x08ProofOps\x12\x32\n\x03ops\x18\x01 \x03(\x0b\x32\x1a.tendermint.crypto.ProofOpB\x04\xc8\xde\x1f\x00R\x03opsB\xbe\x01\n\x15\x63om.tendermint.cryptoB\nProofProtoP\x01Z4github.com/cometbft/cometbft/proto/tendermint/crypto\xa2\x02\x03TCX\xaa\x02\x11Tendermint.Crypto\xca\x02\x11Tendermint\\Crypto\xe2\x02\x1dTendermint\\Crypto\\GPBMetadata\xea\x02\x12Tendermint::Cryptob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.crypto.proof_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.tendermint.cryptoB\nProofProtoP\001Z4github.com/cometbft/cometbft/proto/tendermint/crypto\242\002\003TCX\252\002\021Tendermint.Crypto\312\002\021Tendermint\\Crypto\342\002\035Tendermint\\Crypto\\GPBMetadata\352\002\022Tendermint::Crypto'
  _globals['_PROOFOPS'].fields_by_name['ops']._loaded_options = None
  _globals['_PROOFOPS'].fields_by_name['ops']._serialized_options = b'\310\336\037\000'
  _globals['_PROOF']._serialized_start=74
  _globals['_PROOF']._serialized_end=176
  _globals['_VALUEOP']._serialized_start=178
  _globals['_VALUEOP']._serialized_end=253
  _globals['_DOMINOOP']._serialized_start=255
  _globals['_DOMINOOP']._serialized_end=329
  _globals['_PROOFOP']._serialized_start=331
  _globals['_PROOFOP']._serialized_end=398
  _globals['_PROOFOPS']._serialized_start=400
  _globals['_PROOFOPS']._serialized_end=462
# @@protoc_insertion_point(module_scope)
