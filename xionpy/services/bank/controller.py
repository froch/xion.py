from typing import List, Optional

import grpc

from xionpy.client import XionWallet
from xionpy.client.exceptions import InvalidDenominationError
from xionpy.client.networks import NetworkConfig
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.bank.v1beta1.query_pb2 import (
    QueryAllBalancesRequest,
    QueryBalanceRequest,
    QueryDenomMetadataRequest,
    QueryDenomOwnersRequest,
    QueryDenomsMetadataRequest,
    QueryParamsRequest,
    QuerySendEnabledRequest,
    QuerySpendableBalanceByDenomRequest,
    QuerySpendableBalancesRequest,
    QuerySupplyOfRequest,
    QueryTotalSupplyRequest,
)
from xionpy.protos.cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankGrpcClient
from xionpy.services.bank.messages import msg_send
from xionpy.services.bank.models import (
    CoinModel,
    DenomOwnerModel,
    DenomUnitModel,
    MetadataModel,
    ParamsModel,
    QueryDenomMetadataResponseModel,
    QueryDenomOwnersResponseModel,
    QueryDenomsMetadataResponseModel,
    QueryParamsResponseModel,
    QuerySendEnabledResponseModel,
    QuerySpendableBalanceByDenomResponseModel,
    QuerySpendableBalancesResponseModel,
    QuerySupplyOfResponseModel,
    QueryTotalSupplyResponseModel,
    SendEnabledModel,
)
from xionpy.services.bank.rest import BankRestClient
from xionpy.services.controller import XionBaseController
from xionpy.services.txs.model import Transaction


class XionBankController(XionBaseController):

    def __init__(self, cfg: NetworkConfig, wallet: XionWallet):
        super().__init__(cfg, wallet)
        if isinstance(self.binding, grpc.Channel):
            self.client = BankGrpcClient(self.binding)
        else:
            self.client = BankRestClient(self.binding)

    def query_balances(self, address: Optional[Address] = None, denom: Optional[str] = None) -> int:
        address = address or self.wallet.address()
        denom = denom or self.cfg.denom_fee

        req = QueryBalanceRequest(
            address=str(address),
            denom=denom,
        )

        resp = self.client.Balance(req)
        if resp.balance.denom != denom:
            raise InvalidDenominationError(f"Expected {denom}, got {resp.balance.denom}")

        return int(float(resp.balance.amount))

    def query_all_balances(self, address: Optional[Address] = None) -> List[CoinModel]:
        address = address or self.wallet.address()
        req = QueryAllBalancesRequest(
            address=str(address),
        )

        resp = self.client.AllBalances(req)
        return [CoinModel(denom=coin.denom, amount=coin.amount) for coin in resp.balances]

    def query_denom_metadata(self, denom: Optional[str] = None) -> QueryDenomMetadataResponseModel:
        denom = denom or self.cfg.denom_fee
        req = QueryDenomMetadataRequest(
            denom=denom,
        )

        resp = self.client.DenomMetadata(req)
        return QueryDenomMetadataResponseModel(
            metadata=self._convert_metadata(resp.metadata)
        )

    def query_denoms_metadata(self) -> QueryDenomsMetadataResponseModel:
        req = QueryDenomsMetadataRequest()
        resp = self.client.DenomsMetadata(req)
        return QueryDenomsMetadataResponseModel(
            metadatas=[self._convert_metadata(metadata) for metadata in resp.metadatas]
        )

    def query_denom_owners(self, denom: Optional[str] = None) -> QueryDenomOwnersResponseModel:
        denom = denom or self.cfg.denom_fee
        req = QueryDenomOwnersRequest(
            denom=denom,
        )

        resp = self.client.DenomOwners(req)
        return QueryDenomOwnersResponseModel(
            denom_owners=[
                DenomOwnerModel(
                    address=owner.address,
                    balance=CoinModel(
                        denom=owner.balance.denom,
                        amount=owner.balance.amount,
                    )
                ) for owner in resp.denom_owners
            ]
        )

    def query_total_supply(self) -> QueryTotalSupplyResponseModel:
        req = QueryTotalSupplyRequest()
        resp = self.client.TotalSupply(req)
        return QueryTotalSupplyResponseModel(
            supply=[
                CoinModel(denom=coin.denom, amount=coin.amount) for coin in resp.supply
            ]
        )

    def query_supply_of(self, denom: Optional[str] = None) -> QuerySupplyOfResponseModel:
        denom = denom or self.cfg.denom_fee
        req = QuerySupplyOfRequest(denom=denom)
        resp = self.client.SupplyOf(req)
        return QuerySupplyOfResponseModel(
            amount=CoinModel(denom=resp.amount.denom, amount=resp.amount.amount)
        )

    def query_params(self) -> QueryParamsResponseModel:
        req = QueryParamsRequest()
        resp = self.client.Params(req)
        return QueryParamsResponseModel(
            params=self._convert_params(resp.params)
        )

    def query_send_enabled(self) -> QuerySendEnabledResponseModel:
        req = QuerySendEnabledRequest()
        resp = self.client.SendEnabled(req)
        return QuerySendEnabledResponseModel(
            send_enabled=[self._convert_send_enabled(se) for se in resp.send_enabled]
        )

    def query_spendable_balance_by_denom(self, address: Optional[Address] = None, denom: Optional[str] = None) -> QuerySpendableBalanceByDenomResponseModel:
        address = address or self.wallet.address()
        denom = denom or self.cfg.denom_fee
        req = QuerySpendableBalanceByDenomRequest(
            address=str(address),
            denom=denom,
        )
        resp = self.client.SpendableBalanceByDenom(req)
        return QuerySpendableBalanceByDenomResponseModel(
            balance=CoinModel(denom=resp.balance.denom, amount=resp.balance.amount)
        )

    def query_spendable_balances(self, address: Optional[Address] = None) -> QuerySpendableBalancesResponseModel:
        address = address or self.wallet.address()
        req = QuerySpendableBalancesRequest(
            address=str(address),
        )
        resp = self.client.SpendableBalances(req)
        return QuerySpendableBalancesResponseModel(
            balances=[CoinModel(denom=coin.denom, amount=coin.amount) for coin in resp.balances]
        )

    def tx_send(
            self,
            sender: Optional[Address] = None,
            recipient: Optional[Address] = None,
            amount: Optional[int] = 1_000_000,
            denom: Optional[str] = None,
    ) -> Transaction:
        sender = sender or self.wallet.address()
        recipient = recipient or self.wallet.address()
        denom = denom or self.cfg.denom_fee

        tx = Transaction()
        tx.add_message(
            msg_send(
                from_address=sender,
                to_address=recipient,
                amount=amount,
                denom=denom,
            )
        )
        return tx

    @staticmethod
    def _convert_metadata(metadata) -> MetadataModel:
        return MetadataModel(
            description=metadata.description,
            denom_units=[DenomUnitModel(denom=unit.denom, exponent=unit.exponent, aliases=list(unit.aliases)) for unit in metadata.denom_units],
            base=metadata.base,
            display=metadata.display,
            name=metadata.name,
            symbol=metadata.symbol,
            uri=metadata.uri,
            uri_hash=metadata.uri_hash,
        )

    @staticmethod
    def _convert_params(params) -> ParamsModel:
        return ParamsModel(
            send_enabled=[SendEnabledModel(denom=se.denom, enabled=se.enabled) for se in params.send_enabled],
            default_send_enabled=params.default_send_enabled
        )

    @staticmethod
    def _convert_send_enabled(send_enabled) -> SendEnabledModel:
        return SendEnabledModel(
            denom=send_enabled.denom,
            enabled=send_enabled.enabled
        )
