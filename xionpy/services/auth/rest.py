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
    """Auth REST client."""

    API_URL = "/cosmos/auth/v1beta1"

    def __init__(self, rest_api: XionBaseRestClient) -> None:
        """
        Initialize authentication rest client.

        :param rest_api: RestClient api
        """
        self._rest_api = rest_api

    def Account(self, request: QueryAccountRequest) -> QueryAccountResponse:
        """
        Query account data - sequence, account_id, etc.

        :param request: QueryAccountRequest that contains account address

        :return: QueryAccountResponse
        """
        json_response = self._rest_api.get(f"{self.API_URL}/accounts/{request.address}")
        return Parse(json_response, QueryAccountResponse())

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Query all parameters.

        :param request: QueryParamsRequest

        :return: QueryParamsResponse
        """
        json_response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(json_response, QueryParamsResponse())
