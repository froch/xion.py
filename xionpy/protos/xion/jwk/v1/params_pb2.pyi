from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ("time_offset", "deployment_gas")
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_GAS_FIELD_NUMBER: _ClassVar[int]
    time_offset: int
    deployment_gas: int
    def __init__(self, time_offset: _Optional[int] = ..., deployment_gas: _Optional[int] = ...) -> None: ...
