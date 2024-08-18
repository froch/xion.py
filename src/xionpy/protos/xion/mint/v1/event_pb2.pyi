from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MintIncentiveTokens(_message.Message):
    __slots__ = ("bonded_ratio", "inflation", "annual_provisions", "needed_amount", "collected_amount", "minted_amount", "burned_amount")
    BONDED_RATIO_FIELD_NUMBER: _ClassVar[int]
    INFLATION_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_PROVISIONS_FIELD_NUMBER: _ClassVar[int]
    NEEDED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    COLLECTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MINTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BURNED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    bonded_ratio: str
    inflation: str
    annual_provisions: str
    needed_amount: int
    collected_amount: int
    minted_amount: int
    burned_amount: int
    def __init__(self, bonded_ratio: _Optional[str] = ..., inflation: _Optional[str] = ..., annual_provisions: _Optional[str] = ..., needed_amount: _Optional[int] = ..., collected_amount: _Optional[int] = ..., minted_amount: _Optional[int] = ..., burned_amount: _Optional[int] = ...) -> None: ...
