from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ("params",)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: Params
    def __init__(self, params: _Optional[_Union[Params, _Mapping]] = ...) -> None: ...

class Params(_message.Message):
    __slots__ = ("minimum_gas_prices", "bypass_min_fee_msg_types", "max_total_bypass_min_fee_msg_gas_usage")
    MINIMUM_GAS_PRICES_FIELD_NUMBER: _ClassVar[int]
    BYPASS_MIN_FEE_MSG_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAX_TOTAL_BYPASS_MIN_FEE_MSG_GAS_USAGE_FIELD_NUMBER: _ClassVar[int]
    minimum_gas_prices: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    bypass_min_fee_msg_types: _containers.RepeatedScalarFieldContainer[str]
    max_total_bypass_min_fee_msg_gas_usage: int
    def __init__(self, minimum_gas_prices: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ..., bypass_min_fee_msg_types: _Optional[_Iterable[str]] = ..., max_total_bypass_min_fee_msg_gas_usage: _Optional[int] = ...) -> None: ...
