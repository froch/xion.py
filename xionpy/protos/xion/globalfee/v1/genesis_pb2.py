# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xion/globalfee/v1/genesis.proto
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
    'xion/globalfee/v1/genesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fxion/globalfee/v1/genesis.proto\x12\x11xion.globalfee.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"[\n\x0cGenesisState\x12K\n\x06params\x18\x01 \x01(\x0b\x32\x19.xion.globalfee.v1.ParamsB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10params,omitemptyR\x06params\"\x9c\x03\n\x06Params\x12\xbc\x01\n\x12minimum_gas_prices\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinBp\xc8\xde\x1f\x00\xea\xde\x1f\x1cminimum_gas_prices,omitempty\xf2\xde\x1f\x19yaml:\"minimum_gas_prices\"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoinsR\x10minimumGasPrices\x12\x81\x01\n\x18\x62ypass_min_fee_msg_types\x18\x02 \x03(\tBI\xea\xde\x1f\"bypass_min_fee_msg_types,omitempty\xf2\xde\x1f\x1fyaml:\"bypass_min_fee_msg_types\"R\x14\x62ypassMinFeeMsgTypes\x12O\n&max_total_bypass_min_fee_msg_gas_usage\x18\x03 \x01(\x04R\x1fmaxTotalBypassMinFeeMsgGasUsageB\xb9\x01\n\x15\x63om.xion.globalfee.v1B\x0cGenesisProtoP\x01Z,github.com/burnt-labs/xion/x/globalfee/types\xa2\x02\x03XGX\xaa\x02\x11Xion.Globalfee.V1\xca\x02\x11Xion\\Globalfee\\V1\xe2\x02\x1dXion\\Globalfee\\V1\\GPBMetadata\xea\x02\x13Xion::Globalfee::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xion.globalfee.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.xion.globalfee.v1B\014GenesisProtoP\001Z,github.com/burnt-labs/xion/x/globalfee/types\242\002\003XGX\252\002\021Xion.Globalfee.V1\312\002\021Xion\\Globalfee\\V1\342\002\035Xion\\Globalfee\\V1\\GPBMetadata\352\002\023Xion::Globalfee::V1'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\352\336\037\020params,omitempty'
  _globals['_PARAMS'].fields_by_name['minimum_gas_prices']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['minimum_gas_prices']._serialized_options = b'\310\336\037\000\352\336\037\034minimum_gas_prices,omitempty\362\336\037\031yaml:\"minimum_gas_prices\"\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins'
  _globals['_PARAMS'].fields_by_name['bypass_min_fee_msg_types']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['bypass_min_fee_msg_types']._serialized_options = b'\352\336\037\"bypass_min_fee_msg_types,omitempty\362\336\037\037yaml:\"bypass_min_fee_msg_types\"'
  _globals['_GENESISSTATE']._serialized_start=108
  _globals['_GENESISSTATE']._serialized_end=199
  _globals['_PARAMS']._serialized_start=202
  _globals['_PARAMS']._serialized_end=614
# @@protoc_insertion_point(module_scope)
