# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/circuit/v1/query.proto
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
    'cosmos/circuit/v1/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from cosmos.circuit.v1 import types_pb2 as cosmos_dot_circuit_dot_v1_dot_types__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63osmos/circuit/v1/query.proto\x12\x11\x63osmos.circuit.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1d\x63osmos/circuit/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1b\x63osmos/query/v1/query.proto\"/\n\x13QueryAccountRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\"Q\n\x0f\x41\x63\x63ountResponse\x12>\n\npermission\x18\x01 \x01(\x0b\x32\x1e.cosmos.circuit.v1.PermissionsR\npermission\"^\n\x14QueryAccountsRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xa5\x01\n\x10\x41\x63\x63ountsResponse\x12H\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32,.cosmos.circuit.v1.GenesisAccountPermissionsR\x08\x61\x63\x63ounts\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\x1a\n\x18QueryDisabledListRequest\";\n\x14\x44isabledListResponse\x12#\n\rdisabled_list\x18\x01 \x03(\tR\x0c\x64isabledList2\xad\x03\n\x05Query\x12\x89\x01\n\x07\x41\x63\x63ount\x12&.cosmos.circuit.v1.QueryAccountRequest\x1a\".cosmos.circuit.v1.AccountResponse\"2\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\'\x12%/cosmos/circuit/v1/accounts/{address}\x12\x82\x01\n\x08\x41\x63\x63ounts\x12\'.cosmos.circuit.v1.QueryAccountsRequest\x1a#.cosmos.circuit.v1.AccountsResponse\"(\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/circuit/v1/accounts\x12\x92\x01\n\x0c\x44isabledList\x12+.cosmos.circuit.v1.QueryDisabledListRequest\x1a\'.cosmos.circuit.v1.DisabledListResponse\",\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/circuit/v1/disable_listB\xa7\x01\n\x15\x63om.cosmos.circuit.v1B\nQueryProtoP\x01Z\x1c\x63osmossdk.io/x/circuit/types\xa2\x02\x03\x43\x43X\xaa\x02\x11\x43osmos.Circuit.V1\xca\x02\x11\x43osmos\\Circuit\\V1\xe2\x02\x1d\x43osmos\\Circuit\\V1\\GPBMetadata\xea\x02\x13\x43osmos::Circuit::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.circuit.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.cosmos.circuit.v1B\nQueryProtoP\001Z\034cosmossdk.io/x/circuit/types\242\002\003CCX\252\002\021Cosmos.Circuit.V1\312\002\021Cosmos\\Circuit\\V1\342\002\035Cosmos\\Circuit\\V1\\GPBMetadata\352\002\023Cosmos::Circuit::V1'
  _globals['_QUERY'].methods_by_name['Account']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Account']._serialized_options = b'\210\347\260*\001\202\323\344\223\002\'\022%/cosmos/circuit/v1/accounts/{address}'
  _globals['_QUERY'].methods_by_name['Accounts']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Accounts']._serialized_options = b'\210\347\260*\001\202\323\344\223\002\035\022\033/cosmos/circuit/v1/accounts'
  _globals['_QUERY'].methods_by_name['DisabledList']._loaded_options = None
  _globals['_QUERY'].methods_by_name['DisabledList']._serialized_options = b'\210\347\260*\001\202\323\344\223\002!\022\037/cosmos/circuit/v1/disable_list'
  _globals['_QUERYACCOUNTREQUEST']._serialized_start=186
  _globals['_QUERYACCOUNTREQUEST']._serialized_end=233
  _globals['_ACCOUNTRESPONSE']._serialized_start=235
  _globals['_ACCOUNTRESPONSE']._serialized_end=316
  _globals['_QUERYACCOUNTSREQUEST']._serialized_start=318
  _globals['_QUERYACCOUNTSREQUEST']._serialized_end=412
  _globals['_ACCOUNTSRESPONSE']._serialized_start=415
  _globals['_ACCOUNTSRESPONSE']._serialized_end=580
  _globals['_QUERYDISABLEDLISTREQUEST']._serialized_start=582
  _globals['_QUERYDISABLEDLISTREQUEST']._serialized_end=608
  _globals['_DISABLEDLISTRESPONSE']._serialized_start=610
  _globals['_DISABLEDLISTRESPONSE']._serialized_end=669
  _globals['_QUERY']._serialized_start=672
  _globals['_QUERY']._serialized_end=1101
# @@protoc_insertion_point(module_scope)
