from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueryWebAuthNVerifyRegisterRequest(_message.Message):
    __slots__ = ("addr", "challenge", "rp", "data")
    ADDR_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    RP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    addr: str
    challenge: str
    rp: str
    data: bytes
    def __init__(self, addr: _Optional[str] = ..., challenge: _Optional[str] = ..., rp: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class QueryWebAuthNVerifyRegisterResponse(_message.Message):
    __slots__ = ("credential",)
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    credential: bytes
    def __init__(self, credential: _Optional[bytes] = ...) -> None: ...

class QueryWebAuthNVerifyAuthenticateRequest(_message.Message):
    __slots__ = ("addr", "challenge", "rp", "credential", "data")
    ADDR_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    RP_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    addr: str
    challenge: str
    rp: str
    credential: bytes
    data: bytes
    def __init__(self, addr: _Optional[str] = ..., challenge: _Optional[str] = ..., rp: _Optional[str] = ..., credential: _Optional[bytes] = ..., data: _Optional[bytes] = ...) -> None: ...

class QueryWebAuthNVerifyAuthenticateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
