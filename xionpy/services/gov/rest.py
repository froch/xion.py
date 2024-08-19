from google.protobuf.json_format import Parse

from xionpy.protos.cosmos.gov.v1beta1.query_pb2 import (
    QueryDepositRequest,
    QueryDepositResponse,
    QueryDepositsRequest,
    QueryDepositsResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QueryProposalRequest,
    QueryProposalResponse,
    QueryProposalsRequest,
    QueryProposalsResponse,
    QueryTallyResultRequest,
    QueryTallyResultResponse,
    QueryVoteRequest,
    QueryVoteResponse,
    QueryVotesRequest,
    QueryVotesResponse,
)
from xionpy.services.gov.interface import Gov
from xionpy.services.rest import XionBaseRestClient


class GovRestClient(Gov):
    """Gov REST client."""

    API_URL = "/cosmos/gov/v1beta1"

    def __init__(self, rest_api: XionBaseRestClient) -> None:
        self._rest_api = rest_api

    def Proposal(self, request: QueryProposalRequest) -> QueryProposalResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}",
        )
        return Parse(json_response, QueryProposalResponse())

    def Proposals(self, request: QueryProposalsRequest) -> QueryProposalsResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/",
            request,
        )
        return Parse(json_response, QueryProposalsResponse())

    def Vote(self, request: QueryVoteRequest) -> QueryVoteResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/votes/{request.voter}"
        )
        return Parse(json_response, QueryVoteResponse())

    def Votes(self, request: QueryVotesRequest) -> QueryVotesResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/votes/",
            request,
            ["proposalID"],
        )
        return Parse(json_response, QueryVotesResponse())

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/params/{request.params_type}"
        )
        return Parse(json_response, QueryParamsResponse())

    def Deposit(self, request: QueryDepositRequest) -> QueryDepositResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/deposits/{request.depositor}"
        )
        return Parse(json_response, QueryDepositResponse())

    def Deposits(self, request: QueryDepositsRequest) -> QueryDepositsResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/deposits/",
            request,
            ["proposalID"],
        )
        return Parse(json_response, QueryDepositsResponse())

    def TallyResult(self, request: QueryTallyResultRequest) -> QueryTallyResultResponse:
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/tally"
        )
        return Parse(json_response, QueryTallyResultResponse())
