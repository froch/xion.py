from google.protobuf.json_format import Parse

from xionpy.protos.cosmos.base.tendermint.v1beta1.query_pb2 import (
    GetBlockByHeightRequest,
    GetBlockByHeightResponse,
    GetLatestBlockRequest,
    GetLatestBlockResponse,
    GetLatestValidatorSetRequest,
    GetLatestValidatorSetResponse,
    GetNodeInfoRequest,
    GetNodeInfoResponse,
    GetSyncingRequest,
    GetSyncingResponse,
    GetValidatorSetByHeightRequest,
    GetValidatorSetByHeightResponse,
)
from xionpy.services.rest import XionBaseRestClient


class TendermintRestClient(XionBaseRestClient):
    API_URL = "/cosmos/base/tendermint/v1beta1"

    def __init__(self, rest_api: XionBaseRestClient) -> None:
        self._rest_api = rest_api

    def GetNodeInfo(self, request: GetNodeInfoRequest) -> GetNodeInfoResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/node_info",
        )
        return Parse(json_response, GetNodeInfoResponse())

    def GetSyncing(self, request: GetSyncingRequest) -> GetSyncingResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/syncing",
        )
        return Parse(json_response, GetSyncingResponse())

    def GetLatestBlock(self, request: GetLatestBlockRequest) -> GetLatestBlockResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/blocks/latest",
        )
        return Parse(json_response, GetLatestBlockResponse())

    def GetBlockByHeight(
            self, request: GetBlockByHeightRequest
    ) -> GetBlockByHeightResponse:
        json_response = self._rest_api.get(f"{self.API_URL}/blocks/{request.height}")
        return Parse(json_response, GetBlockByHeightResponse())

    def GetLatestValidatorSet(
            self, request: GetLatestValidatorSetRequest
    ) -> GetLatestValidatorSetResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validatorsets/latest", request
        )
        return Parse(json_response, GetLatestValidatorSetResponse())

    def GetValidatorSetByHeight(
            self, request: GetValidatorSetByHeightRequest
    ) -> GetValidatorSetByHeightResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/validatorsets/{request.height}", request
        )
        return Parse(json_response, GetValidatorSetByHeightResponse())
