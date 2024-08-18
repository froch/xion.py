from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ("platform_percentage",)
    PLATFORM_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    platform_percentage: int
    def __init__(self, platform_percentage: _Optional[int] = ...) -> None: ...
