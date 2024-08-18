from gogoproto import gogo_pb2 as _gogo_pb2
from xion.jwk.v1 import params_pb2 as _params_pb2
from xion.jwk.v1 import audience_pb2 as _audience_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ("params", "audienceList")
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    AUDIENCELIST_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.Params
    audienceList: _containers.RepeatedCompositeFieldContainer[_audience_pb2.Audience]
    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]] = ..., audienceList: _Optional[_Iterable[_Union[_audience_pb2.Audience, _Mapping]]] = ...) -> None: ...
