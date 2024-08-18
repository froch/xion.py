from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from xion.jwk.v1 import params_pb2 as _params_pb2
from xion.jwk.v1 import audience_pb2 as _audience_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ("params",)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.Params
    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryGetAudienceClaimRequest(_message.Message):
    __slots__ = ("hash",)
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    def __init__(self, hash: _Optional[bytes] = ...) -> None: ...

class QueryGetAudienceClaimResponse(_message.Message):
    __slots__ = ("claim",)
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    claim: _audience_pb2.AudienceClaim
    def __init__(self, claim: _Optional[_Union[_audience_pb2.AudienceClaim, _Mapping]] = ...) -> None: ...

class QueryGetAudienceRequest(_message.Message):
    __slots__ = ("aud",)
    AUD_FIELD_NUMBER: _ClassVar[int]
    aud: str
    def __init__(self, aud: _Optional[str] = ...) -> None: ...

class QueryGetAudienceResponse(_message.Message):
    __slots__ = ("audience",)
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    audience: _audience_pb2.Audience
    def __init__(self, audience: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ...) -> None: ...

class QueryAllAudienceRequest(_message.Message):
    __slots__ = ("pagination",)
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryAllAudienceResponse(_message.Message):
    __slots__ = ("audience", "pagination")
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    audience: _containers.RepeatedCompositeFieldContainer[_audience_pb2.Audience]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, audience: _Optional[_Iterable[_Union[_audience_pb2.Audience, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryValidateJWTRequest(_message.Message):
    __slots__ = ("aud", "sub", "sigBytes")
    AUD_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    SIGBYTES_FIELD_NUMBER: _ClassVar[int]
    aud: str
    sub: str
    sigBytes: str
    def __init__(self, aud: _Optional[str] = ..., sub: _Optional[str] = ..., sigBytes: _Optional[str] = ...) -> None: ...

class PrivateClaim(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class QueryValidateJWTResponse(_message.Message):
    __slots__ = ("privateClaims",)
    PRIVATECLAIMS_FIELD_NUMBER: _ClassVar[int]
    privateClaims: _containers.RepeatedCompositeFieldContainer[PrivateClaim]
    def __init__(self, privateClaims: _Optional[_Iterable[_Union[PrivateClaim, _Mapping]]] = ...) -> None: ...
