from typing import List, Optional

import grpc
from google.protobuf.json_format import MessageToDict
from pydantic import TypeAdapter

from xionpy.client import XionWallet
from xionpy.client.networks import NetworkConfig
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.bank.v1beta1.bank_pb2 import Input, Output
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
from xionpy.protos.cosmos.bank.v1beta1.tx_pb2 import MsgMultiSend, MsgSend
from xionpy.protos.cosmos.base.v1beta1.coin_pb2 import Coin
from xionpy.services.bank.models import (
    CoinModel,
    InputModel,
    OutputModel,
    QueryDenomMetadataResponseModel,
    QueryDenomOwnersResponseModel,
    QueryDenomsMetadataResponseModel,
    QueryParamsResponseModel,
    QuerySendEnabledResponseModel,
    QuerySpendableBalanceByDenomResponseModel,
    QuerySpendableBalancesResponseModel,
    QuerySupplyOfResponseModel,
    QueryTotalSupplyResponseModel,
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

    def query_balances(
            self,
            address: Optional[Address] = None,
            denom: Optional[str] = None
    ) -> CoinModel:
        """
        Query the balance of a single denomination for an address.
        :return:
        """

        address = address or self.wallet.address()
        denom = denom or self.cfg.denom_fee

        req = QueryBalanceRequest(
            address=str(address),
            denom=denom,
        )

        resp = self.client.Balance(req)
        data = MessageToDict(resp.balance, preserving_proto_field_name=True)

        return TypeAdapter(
            CoinModel
        ).validate_python(
            data
        )

    def query_all_balances(
            self,
            address: Optional[Address] = None
    ) -> List[CoinModel]:
        """
        Query all balances for an address.
        :return:
        """

        address = address or self.wallet.address()
        req = QueryAllBalancesRequest(
            address=str(address),
        )

        resp = self.client.AllBalances(req)
        data = [
            MessageToDict(coin, preserving_proto_field_name=True)
            for coin in resp.balances
        ]

        return TypeAdapter(
            List[CoinModel]
        ).validate_python(
            data
        )

    def query_denom_metadata(
            self,
            denom: Optional[str] = None
    ) -> QueryDenomMetadataResponseModel:
        """
        Query the metadata of a single denomination.
        :return:
        """

        denom = denom or self.cfg.denom_fee
        req = QueryDenomMetadataRequest(
            denom=denom,
        )

        resp = self.client.DenomMetadata(req)
        data = MessageToDict(resp.metadata, preserving_proto_field_name=True)

        return TypeAdapter(
            QueryDenomMetadataResponseModel
        ).validate_python(
            {"metadata": data}
        )

    def query_denoms_metadata(self) -> QueryDenomsMetadataResponseModel:
        """
        Query the metadata of all denominations.
        :return:
        """

        req = QueryDenomsMetadataRequest()
        resp = self.client.DenomsMetadata(req)
        data = [
            MessageToDict(metadata, preserving_proto_field_name=True)
            for metadata in resp.metadatas
        ]

        return TypeAdapter(
            QueryDenomsMetadataResponseModel
        ).validate_python(
            {"metadatas": data}
        )

    def query_denom_owners(
            self,
            denom: Optional[str] = None
    ) -> QueryDenomOwnersResponseModel:
        """
        Query the owners of a single denomination.
        :return:
        """

        denom = denom or self.cfg.denom_fee
        req = QueryDenomOwnersRequest(
            denom=denom,
        )

        resp = self.client.DenomOwners(req)
        data = [
            MessageToDict(owner, preserving_proto_field_name=True)
            for owner in resp.denom_owners
        ]

        return TypeAdapter(
            QueryDenomOwnersResponseModel
        ).validate_python(
            {"denom_owners": data}
        )

    def query_total_supply(self) -> QueryTotalSupplyResponseModel:
        """
        Query the total supply of all coins.
        :return:
        """

        req = QueryTotalSupplyRequest()
        resp = self.client.TotalSupply(req)
        data = [
            MessageToDict(coin, preserving_proto_field_name=True)
            for coin in resp.supply
        ]

        return TypeAdapter(
            QueryTotalSupplyResponseModel
        ).validate_python(
            {"supply": data}
        )

    def query_supply_of(
            self,
            denom: Optional[str] = None
    ) -> QuerySupplyOfResponseModel:
        """
        Query the supply of a single denomination.
        :return:
        """

        denom = denom or self.cfg.denom_fee
        req = QuerySupplyOfRequest(denom=denom)
        resp = self.client.SupplyOf(req)
        data = MessageToDict(resp.amount, preserving_proto_field_name=True)

        return TypeAdapter(
            QuerySupplyOfResponseModel
        ).validate_python(
            {"amount": data}
        )

    def query_params(self) -> QueryParamsResponseModel:
        """
        Query the bank module parameters.
        :return:
        """

        req = QueryParamsRequest()
        resp = self.client.Params(req)
        data = MessageToDict(resp.params, preserving_proto_field_name=True)

        return TypeAdapter(
            QueryParamsResponseModel
        ).validate_python(
            {"params": data}
        )

    def query_send_enabled(self) -> QuerySendEnabledResponseModel:
        """
        Query whether the bank module is enabled for sending.
        :return:
        """

        req = QuerySendEnabledRequest()
        resp = self.client.SendEnabled(req)
        send_enabled_data = [
            MessageToDict(se, preserving_proto_field_name=True)
            for se in resp.send_enabled
        ]

        return TypeAdapter(
            QuerySendEnabledResponseModel
        ).validate_python(
            {"send_enabled": send_enabled_data}
        )

    def query_spendable_balance_by_denom(
            self,
            address: Optional[Address] = None,
            denom: Optional[str] = None,
    ) -> QuerySpendableBalanceByDenomResponseModel:
        """
        Query the spendable balance of a single denomination for an address.
        :return:
        """

        address = address or self.wallet.address()
        denom = denom or self.cfg.denom_fee

        req = QuerySpendableBalanceByDenomRequest(
            address=str(address),
            denom=denom,
        )
        resp = self.client.SpendableBalanceByDenom(req)
        data = MessageToDict(resp.balance, preserving_proto_field_name=True)

        return TypeAdapter(
            QuerySpendableBalanceByDenomResponseModel
        ).validate_python(
            {"balance": data}
        )

    def query_spendable_balances(
            self,
            address: Optional[Address] = None
    ) -> QuerySpendableBalancesResponseModel:
        """
        Query the spendable balances of all denominations for an address.
        :return:
        """

        address = address or self.wallet.address()

        req = QuerySpendableBalancesRequest(
            address=str(address),
        )
        resp = self.client.SpendableBalances(req)
        data = [
            MessageToDict(coin, preserving_proto_field_name=True)
            for coin in resp.balances
        ]

        return TypeAdapter(
            QuerySpendableBalancesResponseModel
        ).validate_python(
            {"balances": data}
        )

    def tx_bank_send(
            self,
            sender: Optional[Address] = None,
            recipient: Optional[Address] = None,
            amount: Optional[int] = 1_000_000,
            denom: Optional[str] = None,
    ) -> Transaction:
        """
        Create a transaction to send coins from one account to another.
        :return:
        """

        sender = sender or self.wallet.address()
        recipient = recipient or self.wallet.address()
        denom = denom or self.cfg.denom_fee

        msg = MsgSend(
            from_address=str(sender),
            to_address=str(recipient),
            amount=[Coin(amount=str(amount), denom=denom)],
        )

        tx = Transaction()
        tx.add_message(msg)
        return tx

    def tx_bank_multi_send(
            self,
            inputs: List[InputModel],
            outputs: List[OutputModel]
    ) -> Transaction:
        """
        Create a transaction to send coins from multiple accounts to multiple accounts.
        :return:
        """

        msg_inputs = [
            Input(
                address=input_.address,
                coins=[
                    Coin(denom=coin.denom, amount=str(coin.amount))
                    for coin in input_.coins
                ],
            ) for input_ in inputs
        ]
        msg_outputs = [
            Output(
                address=output.address,
                coins=[
                    Coin(denom=coin.denom, amount=str(coin.amount))
                    for coin in output.coins
                ],
            ) for output in outputs
        ]

        msg = MsgMultiSend(
            inputs=msg_inputs,
            outputs=msg_outputs,
        )

        tx = Transaction()
        tx.add_message(msg)
        return tx
