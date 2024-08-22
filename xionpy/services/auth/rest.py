from google.protobuf.json_format import Parse

from xionpy.protos.cosmos.auth.v1beta1.query_pb2 import (
    QueryAccountRequest,
    QueryAccountResponse,
    QueryParamsRequest,
    QueryParamsResponse,
)
from xionpy.services.auth.interface import Auth
from xionpy.services.rest import XionBaseRestClient


class AuthRestClient(Auth):

    API_URL = "/cosmos/auth/v1beta1"

    def __init__(self, rest_api: XionBaseRestClient) -> None:
        self._rest_api = rest_api

    def Account(self, request: QueryAccountRequest) -> QueryAccountResponse:
        json_response = self._rest_api.get(f"{self.API_URL}/accounts/{request.address}")
        return Parse(json_response, QueryAccountResponse())

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        json_response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(json_response, QueryParamsResponse())
