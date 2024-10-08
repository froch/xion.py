import base64
import json
from typing import Any, Dict, List

from google.protobuf.json_format import Parse, ParseDict

from xionpy.protos.cosmos.crypto.secp256k1.keys_pb2 import (  # noqa: F401  # pylint: disable=unused-import
    PubKey as ProtoPubKey,
)
from xionpy.protos.cosmos.tx.v1beta1.service_pb2 import (
    BroadcastTxRequest,
    BroadcastTxResponse,
    GetTxRequest,
    GetTxResponse,
    GetTxsEventRequest,
    GetTxsEventResponse,
    SimulateRequest,
    SimulateResponse,
)
from xionpy.protos.cosmwasm.wasm.v1.tx_pb2 import (  # noqa: F401  # pylint: disable=unused-import
    MsgExecuteContract,
    MsgInstantiateContract,
    MsgStoreCode,
)
from xionpy.services.rest import XionBaseRestClient
from xionpy.services.txs.interface import TxInterface
from xionpy.services.utils import json_encode


# Unused imports are required to make sure that related types get generated
# Parse and ParseDict fail without them


class TxsRestClient(TxInterface):

    API_URL = "/cosmos/tx/v1beta1"

    def __init__(self, rest_client: XionBaseRestClient) -> None:
        self.rest_client = rest_client

    def Simulate(self, request: SimulateRequest) -> SimulateResponse:
        response = self.rest_client.post(
            f"{self.API_URL}/simulate",
            request,
        )
        return Parse(response, SimulateResponse())

    def GetTx(self, request: GetTxRequest) -> GetTxResponse:
        response = self.rest_client.get(f"{self.API_URL}/txs/{request.hash}")

        # JSON in case of CosmWasm messages workaround
        dict_response = json.loads(response)
        self._fix_messages(dict_response["tx"]["body"]["messages"])
        self._fix_messages(dict_response["tx_response"]["tx"]["body"]["messages"])

        return ParseDict(dict_response, GetTxResponse())

    def BroadcastTx(self, request: BroadcastTxRequest) -> BroadcastTxResponse:
        response = self.rest_client.post(f"{self.API_URL}/txs", request)
        return Parse(response, BroadcastTxResponse())

    def GetTxsEvent(self, request: GetTxsEventRequest) -> GetTxsEventResponse:
        response = self.rest_client.get(f"{self.API_URL}/txs", request)

        # JSON in case of CosmWasm messages workaround
        dict_response = json.loads(response)
        for tx in dict_response["txs"]:
            self._fix_messages(tx["body"]["messages"])

        for tx_response in dict_response["tx_responses"]:
            self._fix_messages(tx_response["tx"]["body"]["messages"])

        return ParseDict(dict_response, GetTxsEventResponse())

    @staticmethod
    def _fix_messages(messages: List[Dict[str, Any]]):
        """
        Fix for REST api response in case of CosmWasm messages contains dict instead of base64 encoded string.
        :param messages: List of message in Tx response
        """
        for message in messages:
            if message["@type"] == "/cosmwasm.wasm.v1.MsgInstantiateContract":
                message["msg"] = base64.b64encode(
                    json_encode(message["msg"]).encode("UTF8")
                ).decode()
            if message["@type"] == "/cosmwasm.wasm.v1.MsgExecuteContract":
                message["msg"] = base64.b64encode(
                    json_encode(message["msg"]).encode("UTF8")
                ).decode()
            if message["@type"] == "/cosmwasm.wasm.v1.MsgMigrateContract":
                message["msg"] = base64.b64encode(
                    json_encode(message["msg"]).encode("UTF8")
                ).decode()
