from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from amino import amino_pb2 as _amino_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthzAllowance(_message.Message):
    __slots__ = ("allowance", "authz_grantee")
    ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    AUTHZ_GRANTEE_FIELD_NUMBER: _ClassVar[int]
    allowance: _any_pb2.Any
    authz_grantee: str
    def __init__(self, allowance: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., authz_grantee: _Optional[str] = ...) -> None: ...

class ContractsAllowance(_message.Message):
    __slots__ = ("allowance", "contract_addresses")
    ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    allowance: _any_pb2.Any
    contract_addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allowance: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., contract_addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class MultiAnyAllowance(_message.Message):
    __slots__ = ("allowances",)
    ALLOWANCES_FIELD_NUMBER: _ClassVar[int]
    allowances: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, allowances: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
