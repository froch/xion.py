# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xion/v1/tx.proto
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
    'xion/v1/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from amino import amino_pb2 as amino_dot_amino__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10xion/v1/tx.proto\x12\x07xion.v1\x1a\x14gogoproto/gogo.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\"\x95\x02\n\x07MsgSend\x12;\n\x0c\x66rom_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0b\x66romAddress\x12\x37\n\nto_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\ttoAddress\x12h\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01R\x06\x61mount:*\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x0c\x66rom_address\x8a\xe7\xb0*\x0cxion/MsgSend\"\x11\n\x0fMsgSendResponse\"\xb6\x01\n\x0cMsgMultiSend\x12=\n\x06inputs\x18\x01 \x03(\x0b\x32\x1a.cosmos.bank.v1beta1.InputB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06inputs\x12@\n\x07outputs\x18\x02 \x03(\x0b\x32\x1b.cosmos.bank.v1beta1.OutputB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07outputs:%\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06inputs\x8a\xe7\xb0*\x11xion/MsgMultiSend\"\x16\n\x14MsgMultiSendResponse\"\xb5\x01\n\x18MsgSetPlatformPercentage\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12/\n\x13platform_percentage\x18\x02 \x01(\rR\x12platformPercentage:0\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1dxion/MsgSetPlatformPercentage\"\"\n MsgSetPlatformPercentageResponse2\xea\x01\n\x03Msg\x12\x32\n\x04Send\x12\x10.xion.v1.MsgSend\x1a\x18.xion.v1.MsgSendResponse\x12\x41\n\tMultiSend\x12\x15.xion.v1.MsgMultiSend\x1a\x1d.xion.v1.MsgMultiSendResponse\x12\x65\n\x15SetPlatformPercentage\x12!.xion.v1.MsgSetPlatformPercentage\x1a).xion.v1.MsgSetPlatformPercentageResponse\x1a\x05\x80\xe7\xb0*\x01\x42|\n\x0b\x63om.xion.v1B\x07TxProtoP\x01Z\'github.com/burnt-labs/xion/x/xion/types\xa2\x02\x03XXX\xaa\x02\x07Xion.V1\xca\x02\x07Xion\\V1\xe2\x02\x13Xion\\V1\\GPBMetadata\xea\x02\x08Xion::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xion.v1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\013com.xion.v1B\007TxProtoP\001Z\'github.com/burnt-labs/xion/x/xion/types\242\002\003XXX\252\002\007Xion.V1\312\002\007Xion\\V1\342\002\023Xion\\V1\\GPBMetadata\352\002\010Xion::V1'
  _globals['_MSGSEND'].fields_by_name['from_address']._loaded_options = None
  _globals['_MSGSEND'].fields_by_name['from_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSEND'].fields_by_name['to_address']._loaded_options = None
  _globals['_MSGSEND'].fields_by_name['to_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSEND'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGSEND'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _globals['_MSGSEND']._loaded_options = None
  _globals['_MSGSEND']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\014from_address\212\347\260*\014xion/MsgSend'
  _globals['_MSGMULTISEND'].fields_by_name['inputs']._loaded_options = None
  _globals['_MSGMULTISEND'].fields_by_name['inputs']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGMULTISEND'].fields_by_name['outputs']._loaded_options = None
  _globals['_MSGMULTISEND'].fields_by_name['outputs']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGMULTISEND']._loaded_options = None
  _globals['_MSGMULTISEND']._serialized_options = b'\350\240\037\000\202\347\260*\006inputs\212\347\260*\021xion/MsgMultiSend'
  _globals['_MSGSETPLATFORMPERCENTAGE'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGSETPLATFORMPERCENTAGE'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSETPLATFORMPERCENTAGE']._loaded_options = None
  _globals['_MSGSETPLATFORMPERCENTAGE']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\035xion/MsgSetPlatformPercentage'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSEND']._serialized_start=187
  _globals['_MSGSEND']._serialized_end=464
  _globals['_MSGSENDRESPONSE']._serialized_start=466
  _globals['_MSGSENDRESPONSE']._serialized_end=483
  _globals['_MSGMULTISEND']._serialized_start=486
  _globals['_MSGMULTISEND']._serialized_end=668
  _globals['_MSGMULTISENDRESPONSE']._serialized_start=670
  _globals['_MSGMULTISENDRESPONSE']._serialized_end=692
  _globals['_MSGSETPLATFORMPERCENTAGE']._serialized_start=695
  _globals['_MSGSETPLATFORMPERCENTAGE']._serialized_end=876
  _globals['_MSGSETPLATFORMPERCENTAGERESPONSE']._serialized_start=878
  _globals['_MSGSETPLATFORMPERCENTAGERESPONSE']._serialized_end=912
  _globals['_MSG']._serialized_start=915
  _globals['_MSG']._serialized_end=1149
# @@protoc_insertion_point(module_scope)
