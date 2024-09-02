import grpc
from google.protobuf.json_format import MessageToDict
from pydantic import TypeAdapter

from xionpy.client import NetworkConfig
from xionpy.protos.cosmos.base.tendermint.v1beta1.query_pb2 import (
    GetBlockByHeightRequest,
    GetLatestBlockRequest,
    GetLatestValidatorSetRequest,
    GetNodeInfoRequest,
    GetSyncingRequest,
    GetValidatorSetByHeightRequest,
)
from xionpy.protos.cosmos.base.tendermint.v1beta1.query_pb2_grpc import (
    ServiceStub as TendermintGrpcClient,
)
from xionpy.services.base.tendermint.models import (
    GetBlockByHeightResponseModel,
    GetLatestBlockResponseModel,
    GetLatestValidatorSetResponseModel,
    GetNodeInfoResponseModel,
    GetSyncingResponseModel,
    GetValidatorSetByHeightResponseModel,
)
from xionpy.services.base.tendermint.rest import TendermintRestClient
from xionpy.services.controller import XionBaseController


class XionTendermintController(XionBaseController):

    def __init__(
            self,
            cfg: NetworkConfig | None = None
    ):
        super().__init__(cfg)
        if isinstance(self.binding, grpc.Channel):
            self.client = TendermintGrpcClient(self.binding)
        else:
            self.client = TendermintRestClient(self.binding)

    def query_node_info(self) -> GetNodeInfoResponseModel:
        """
        Queries the current node's info.
        :return:
        """

        response = self.client.GetNodeInfo(GetNodeInfoRequest())
        data = MessageToDict(response, preserving_proto_field_name=True)

        return TypeAdapter(
            GetNodeInfoResponseModel
        ).validate_python(
            data
        )

    def query_syncing(self) -> GetSyncingResponseModel:
        """
        Queries the current node's syncing status.
        :return:
        """

        response = self.client.GetSyncing(GetSyncingRequest())
        data = MessageToDict(response, preserving_proto_field_name=True)

        return TypeAdapter(
            GetSyncingResponseModel
        ).validate_python(
            data
        )

    def query_latest_block(self) -> GetLatestBlockResponseModel:
        """
        Fetches the latest block
        :return:
        """

        response = self.client.GetLatestBlock(GetLatestBlockRequest())
        data = MessageToDict(response, preserving_proto_field_name=True)

        return TypeAdapter(
            GetLatestBlockResponseModel
        ).validate_python(
            data
        )

    def query_block_by_height(self, height: int | None = None) -> GetBlockByHeightResponseModel:
        """
        GetBlockByHeight queries block for given height.
        :return:
        """

        req = GetBlockByHeightRequest(height=height)
        response = self.client.GetBlockByHeight(req)
        data = MessageToDict(response, preserving_proto_field_name=True)

        return TypeAdapter(
            GetBlockByHeightResponseModel
        ).validate_python(
            data
        )

    def query_latest_validator_set(self) -> GetLatestValidatorSetResponseModel:
        """
        Fetch the latest validator set
        :return:
        """

        req = GetLatestValidatorSetRequest()
        response = self.client.GetLatestValidatorSet(req)
        data = MessageToDict(response, preserving_proto_field_name=True)

        return TypeAdapter(
            GetLatestValidatorSetResponseModel
        ).validate_python(
            data
        )

    def query_validators_by_height(self, height: int) -> GetValidatorSetByHeightResponseModel:
        """
        Fetch the validator set at the given height
        :return:
        """

        req = GetValidatorSetByHeightRequest(height=height)
        response = self.client.GetValidatorSetByHeight(req)
        data = MessageToDict(response, preserving_proto_field_name=True)

        return TypeAdapter(
            GetValidatorSetByHeightResponseModel
        ).validate_python(
            data
        )
