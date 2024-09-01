from typing import List, Optional

from pydantic import BaseModel

from xionpy.services.base.coin.model import CoinModel


class SendAuthorizationModel(BaseModel):
    spend_limit: List[CoinModel]
    allow_list: Optional[List[str]] = None


class ParamsModel(BaseModel):
    send_enabled: List["SendEnabledModel"]
    default_send_enabled: bool


class SendEnabledModel(BaseModel):
    denom: str
    enabled: bool


class InputModel(BaseModel):
    address: str
    coins: List[CoinModel]


class OutputModel(BaseModel):
    address: str
    coins: List[CoinModel]


class SupplyModel(BaseModel):
    total: List[CoinModel]


class DenomUnitModel(BaseModel):
    denom: str
    exponent: int
    aliases: Optional[List[str]] = None


class MetadataModel(BaseModel):
    description: Optional[str] = None
    denom_units: List[DenomUnitModel]
    base: str
    display: str
    name: Optional[str] = None
    symbol: Optional[str] = None
    uri: Optional[str] = None
    uri_hash: Optional[str] = None


class BalanceModel(BaseModel):
    address: str
    coins: List[CoinModel]


class GenesisStateModel(BaseModel):
    params: ParamsModel
    balances: List[BalanceModel]
    supply: List[CoinModel]
    denom_metadata: List[MetadataModel]
    send_enabled: List[SendEnabledModel]


class QueryBalanceRequestModel(BaseModel):
    address: str
    denom: str


class QueryBalanceResponseModel(BaseModel):
    balance: CoinModel


class QueryAllBalancesRequestModel(BaseModel):
    address: str
    resolve_denom: Optional[bool] = None


class QueryAllBalancesResponseModel(BaseModel):
    balances: List[CoinModel]
    pagination: Optional[str] = None


class QuerySpendableBalanceByDenomResponseModel(BaseModel):
    balance: CoinModel


class QuerySpendableBalancesRequestModel(BaseModel):
    address: str
    pagination: Optional[str] = None


class QuerySpendableBalancesResponseModel(BaseModel):
    balances: List[CoinModel]
    pagination: Optional[str] = None


class QueryTotalSupplyRequestModel(BaseModel):
    pagination: Optional[str] = None


class QueryTotalSupplyResponseModel(BaseModel):
    supply: List[CoinModel]
    pagination: Optional[str] = None


class QuerySupplyOfRequestModel(BaseModel):
    denom: str


class QuerySupplyOfResponseModel(BaseModel):
    amount: CoinModel


class QueryParamsRequestModel(BaseModel):
    pass


class QueryParamsResponseModel(BaseModel):
    params: ParamsModel


class QueryDenomsMetadataRequestModel(BaseModel):
    pagination: Optional[str] = None


class QueryDenomsMetadataResponseModel(BaseModel):
    metadatas: List[MetadataModel]
    pagination: Optional[str] = None


class QueryDenomMetadataRequestModel(BaseModel):
    denom: str


class QueryDenomMetadataResponseModel(BaseModel):
    metadata: MetadataModel


class QueryDenomOwnersRequestModel(BaseModel):
    denom: str
    pagination: Optional[str] = None


class DenomOwnerModel(BaseModel):
    address: str
    balance: CoinModel


class QueryDenomOwnersResponseModel(BaseModel):
    denom_owners: List[DenomOwnerModel]
    pagination: Optional[str] = None


class QuerySendEnabledRequestModel(BaseModel):
    denoms: Optional[List[str]] = None
    pagination: Optional[str] = None


class QuerySendEnabledResponseModel(BaseModel):
    send_enabled: List[SendEnabledModel]
    pagination: Optional[str] = None
