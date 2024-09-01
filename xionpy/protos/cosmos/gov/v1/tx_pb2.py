# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/gov/v1/tx.proto
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
    'cosmos/gov/v1/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.gov.v1 import gov_pb2 as cosmos_dot_gov_dot_v1_dot_gov__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from amino import amino_pb2 as amino_dot_amino__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63osmos/gov/v1/tx.proto\x12\rcosmos.gov.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/gov/v1/gov.proto\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa5\x03\n\x11MsgSubmitProposal\x12\x30\n\x08messages\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyR\x08messages\x12\x8a\x01\n\x0finitial_deposit\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x0einitialDeposit\x12\x34\n\x08proposer\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08proposer\x12\x1a\n\x08metadata\x18\x04 \x01(\tR\x08metadata\x12\x14\n\x05title\x18\x05 \x01(\tR\x05title\x12\x18\n\x07summary\x18\x06 \x01(\tR\x07summary\x12\x1c\n\texpedited\x18\x07 \x01(\x08R\texpedited:1\x82\xe7\xb0*\x08proposer\x8a\xe7\xb0*\x1f\x63osmos-sdk/v1/MsgSubmitProposal\"<\n\x19MsgSubmitProposalResponse\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\"\xbb\x01\n\x14MsgExecLegacyContent\x12N\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x1e\xca\xb4-\x1a\x63osmos.gov.v1beta1.ContentR\x07\x63ontent\x12\x1c\n\tauthority\x18\x02 \x01(\tR\tauthority:5\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\"cosmos-sdk/v1/MsgExecLegacyContent\"\x1e\n\x1cMsgExecLegacyContentResponse\"\xe5\x01\n\x07MsgVote\x12\x35\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x14\xea\xde\x1f\x0bproposal_id\xa8\xe7\xb0*\x01R\nproposalId\x12.\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05voter\x12\x31\n\x06option\x18\x03 \x01(\x0e\x32\x19.cosmos.gov.v1.VoteOptionR\x06option\x12\x1a\n\x08metadata\x18\x04 \x01(\tR\x08metadata:$\x82\xe7\xb0*\x05voter\x8a\xe7\xb0*\x15\x63osmos-sdk/v1/MsgVote\"\x11\n\x0fMsgVoteResponse\"\xff\x01\n\x0fMsgVoteWeighted\x12\x35\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x14\xea\xde\x1f\x0bproposal_id\xa8\xe7\xb0*\x01R\nproposalId\x12.\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05voter\x12;\n\x07options\x18\x03 \x03(\x0b\x32!.cosmos.gov.v1.WeightedVoteOptionR\x07options\x12\x1a\n\x08metadata\x18\x04 \x01(\tR\x08metadata:,\x82\xe7\xb0*\x05voter\x8a\xe7\xb0*\x1d\x63osmos-sdk/v1/MsgVoteWeighted\"\x19\n\x17MsgVoteWeightedResponse\"\xe6\x01\n\nMsgDeposit\x12\x35\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x14\xea\xde\x1f\x0bproposal_id\xa8\xe7\xb0*\x01R\nproposalId\x12\x36\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tdepositor\x12<\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06\x61mount:+\x82\xe7\xb0*\tdepositor\x8a\xe7\xb0*\x18\x63osmos-sdk/v1/MsgDeposit\"\x14\n\x12MsgDepositResponse\"\xbb\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x38\n\x06params\x18\x02 \x01(\x0b\x32\x15.cosmos.gov.v1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params:6\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*#cosmos-sdk/x/gov/v1/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\x8a\x01\n\x11MsgCancelProposal\x12\x30\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x0f\xea\xde\x1f\x0bproposal_idR\nproposalId\x12\x34\n\x08proposer\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08proposer:\r\x82\xe7\xb0*\x08proposer\"\xc1\x01\n\x19MsgCancelProposalResponse\x12\x30\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x0f\xea\xde\x1f\x0bproposal_idR\nproposalId\x12I\n\rcanceled_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x0c\x63\x61nceledTime\x12\'\n\x0f\x63\x61nceled_height\x18\x03 \x01(\x04R\x0e\x63\x61nceledHeight2\xe8\x04\n\x03Msg\x12\\\n\x0eSubmitProposal\x12 .cosmos.gov.v1.MsgSubmitProposal\x1a(.cosmos.gov.v1.MsgSubmitProposalResponse\x12\x65\n\x11\x45xecLegacyContent\x12#.cosmos.gov.v1.MsgExecLegacyContent\x1a+.cosmos.gov.v1.MsgExecLegacyContentResponse\x12>\n\x04Vote\x12\x16.cosmos.gov.v1.MsgVote\x1a\x1e.cosmos.gov.v1.MsgVoteResponse\x12V\n\x0cVoteWeighted\x12\x1e.cosmos.gov.v1.MsgVoteWeighted\x1a&.cosmos.gov.v1.MsgVoteWeightedResponse\x12G\n\x07\x44\x65posit\x12\x19.cosmos.gov.v1.MsgDeposit\x1a!.cosmos.gov.v1.MsgDepositResponse\x12V\n\x0cUpdateParams\x12\x1e.cosmos.gov.v1.MsgUpdateParams\x1a&.cosmos.gov.v1.MsgUpdateParamsResponse\x12\\\n\x0e\x43\x61ncelProposal\x12 .cosmos.gov.v1.MsgCancelProposal\x1a(.cosmos.gov.v1.MsgCancelProposalResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x9f\x01\n\x11\x63om.cosmos.gov.v1B\x07TxProtoP\x01Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1\xa2\x02\x03\x43GX\xaa\x02\rCosmos.Gov.V1\xca\x02\rCosmos\\Gov\\V1\xe2\x02\x19\x43osmos\\Gov\\V1\\GPBMetadata\xea\x02\x0f\x43osmos::Gov::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.cosmos.gov.v1B\007TxProtoP\001Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1\242\002\003CGX\252\002\rCosmos.Gov.V1\312\002\rCosmos\\Gov\\V1\342\002\031Cosmos\\Gov\\V1\\GPBMetadata\352\002\017Cosmos::Gov::V1'
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['initial_deposit']._loaded_options = None
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['initial_deposit']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['proposer']._loaded_options = None
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['proposer']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSUBMITPROPOSAL']._loaded_options = None
  _globals['_MSGSUBMITPROPOSAL']._serialized_options = b'\202\347\260*\010proposer\212\347\260*\037cosmos-sdk/v1/MsgSubmitProposal'
  _globals['_MSGEXECLEGACYCONTENT'].fields_by_name['content']._loaded_options = None
  _globals['_MSGEXECLEGACYCONTENT'].fields_by_name['content']._serialized_options = b'\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_MSGEXECLEGACYCONTENT']._loaded_options = None
  _globals['_MSGEXECLEGACYCONTENT']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\"cosmos-sdk/v1/MsgExecLegacyContent'
  _globals['_MSGVOTE'].fields_by_name['proposal_id']._loaded_options = None
  _globals['_MSGVOTE'].fields_by_name['proposal_id']._serialized_options = b'\352\336\037\013proposal_id\250\347\260*\001'
  _globals['_MSGVOTE'].fields_by_name['voter']._loaded_options = None
  _globals['_MSGVOTE'].fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGVOTE']._loaded_options = None
  _globals['_MSGVOTE']._serialized_options = b'\202\347\260*\005voter\212\347\260*\025cosmos-sdk/v1/MsgVote'
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['proposal_id']._loaded_options = None
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['proposal_id']._serialized_options = b'\352\336\037\013proposal_id\250\347\260*\001'
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['voter']._loaded_options = None
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGVOTEWEIGHTED']._loaded_options = None
  _globals['_MSGVOTEWEIGHTED']._serialized_options = b'\202\347\260*\005voter\212\347\260*\035cosmos-sdk/v1/MsgVoteWeighted'
  _globals['_MSGDEPOSIT'].fields_by_name['proposal_id']._loaded_options = None
  _globals['_MSGDEPOSIT'].fields_by_name['proposal_id']._serialized_options = b'\352\336\037\013proposal_id\250\347\260*\001'
  _globals['_MSGDEPOSIT'].fields_by_name['depositor']._loaded_options = None
  _globals['_MSGDEPOSIT'].fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGDEPOSIT'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGDEPOSIT'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGDEPOSIT']._loaded_options = None
  _globals['_MSGDEPOSIT']._serialized_options = b'\202\347\260*\tdepositor\212\347\260*\030cosmos-sdk/v1/MsgDeposit'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*#cosmos-sdk/x/gov/v1/MsgUpdateParams'
  _globals['_MSGCANCELPROPOSAL'].fields_by_name['proposal_id']._loaded_options = None
  _globals['_MSGCANCELPROPOSAL'].fields_by_name['proposal_id']._serialized_options = b'\352\336\037\013proposal_id'
  _globals['_MSGCANCELPROPOSAL'].fields_by_name['proposer']._loaded_options = None
  _globals['_MSGCANCELPROPOSAL'].fields_by_name['proposer']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGCANCELPROPOSAL']._loaded_options = None
  _globals['_MSGCANCELPROPOSAL']._serialized_options = b'\202\347\260*\010proposer'
  _globals['_MSGCANCELPROPOSALRESPONSE'].fields_by_name['proposal_id']._loaded_options = None
  _globals['_MSGCANCELPROPOSALRESPONSE'].fields_by_name['proposal_id']._serialized_options = b'\352\336\037\013proposal_id'
  _globals['_MSGCANCELPROPOSALRESPONSE'].fields_by_name['canceled_time']._loaded_options = None
  _globals['_MSGCANCELPROPOSALRESPONSE'].fields_by_name['canceled_time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSUBMITPROPOSAL']._serialized_start=252
  _globals['_MSGSUBMITPROPOSAL']._serialized_end=673
  _globals['_MSGSUBMITPROPOSALRESPONSE']._serialized_start=675
  _globals['_MSGSUBMITPROPOSALRESPONSE']._serialized_end=735
  _globals['_MSGEXECLEGACYCONTENT']._serialized_start=738
  _globals['_MSGEXECLEGACYCONTENT']._serialized_end=925
  _globals['_MSGEXECLEGACYCONTENTRESPONSE']._serialized_start=927
  _globals['_MSGEXECLEGACYCONTENTRESPONSE']._serialized_end=957
  _globals['_MSGVOTE']._serialized_start=960
  _globals['_MSGVOTE']._serialized_end=1189
  _globals['_MSGVOTERESPONSE']._serialized_start=1191
  _globals['_MSGVOTERESPONSE']._serialized_end=1208
  _globals['_MSGVOTEWEIGHTED']._serialized_start=1211
  _globals['_MSGVOTEWEIGHTED']._serialized_end=1466
  _globals['_MSGVOTEWEIGHTEDRESPONSE']._serialized_start=1468
  _globals['_MSGVOTEWEIGHTEDRESPONSE']._serialized_end=1493
  _globals['_MSGDEPOSIT']._serialized_start=1496
  _globals['_MSGDEPOSIT']._serialized_end=1726
  _globals['_MSGDEPOSITRESPONSE']._serialized_start=1728
  _globals['_MSGDEPOSITRESPONSE']._serialized_end=1748
  _globals['_MSGUPDATEPARAMS']._serialized_start=1751
  _globals['_MSGUPDATEPARAMS']._serialized_end=1938
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=1940
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=1965
  _globals['_MSGCANCELPROPOSAL']._serialized_start=1968
  _globals['_MSGCANCELPROPOSAL']._serialized_end=2106
  _globals['_MSGCANCELPROPOSALRESPONSE']._serialized_start=2109
  _globals['_MSGCANCELPROPOSALRESPONSE']._serialized_end=2302
  _globals['_MSG']._serialized_start=2305
  _globals['_MSG']._serialized_end=2921
# @@protoc_insertion_point(module_scope)
