from xion.jwk.v1 import audience_pb2 as _audience_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateAudienceClaim(_message.Message):
    __slots__ = ("admin", "aud_hash")
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUD_HASH_FIELD_NUMBER: _ClassVar[int]
    admin: str
    aud_hash: bytes
    def __init__(self, admin: _Optional[str] = ..., aud_hash: _Optional[bytes] = ...) -> None: ...

class MsgCreateAudienceClaimResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MsgDeleteAudienceClaim(_message.Message):
    __slots__ = ("admin", "aud_hash")
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUD_HASH_FIELD_NUMBER: _ClassVar[int]
    admin: str
    aud_hash: bytes
    def __init__(self, admin: _Optional[str] = ..., aud_hash: _Optional[bytes] = ...) -> None: ...

class MsgDeleteAudienceClaimResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MsgCreateAudience(_message.Message):
    __slots__ = ("admin", "aud", "key")
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUD_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    admin: str
    aud: str
    key: str
    def __init__(self, admin: _Optional[str] = ..., aud: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class MsgCreateAudienceResponse(_message.Message):
    __slots__ = ("audience",)
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    audience: _audience_pb2.Audience
    def __init__(self, audience: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ...) -> None: ...

class MsgUpdateAudience(_message.Message):
    __slots__ = ("admin", "new_admin", "aud", "key")
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    NEW_ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUD_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    admin: str
    new_admin: str
    aud: str
    key: str
    def __init__(self, admin: _Optional[str] = ..., new_admin: _Optional[str] = ..., aud: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class MsgUpdateAudienceResponse(_message.Message):
    __slots__ = ("audience",)
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    audience: _audience_pb2.Audience
    def __init__(self, audience: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ...) -> None: ...

class MsgDeleteAudience(_message.Message):
    __slots__ = ("admin", "aud")
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUD_FIELD_NUMBER: _ClassVar[int]
    admin: str
    aud: str
    def __init__(self, admin: _Optional[str] = ..., aud: _Optional[str] = ...) -> None: ...

class MsgDeleteAudienceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
