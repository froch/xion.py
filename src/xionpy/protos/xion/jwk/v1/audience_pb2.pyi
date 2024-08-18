from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Audience(_message.Message):
    __slots__ = ("aud", "key", "admin")
    AUD_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    aud: str
    key: str
    admin: str
    def __init__(self, aud: _Optional[str] = ..., key: _Optional[str] = ..., admin: _Optional[str] = ...) -> None: ...

class AudienceClaim(_message.Message):
    __slots__ = ("signer",)
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    signer: str
    def __init__(self, signer: _Optional[str] = ...) -> None: ...
