from typing import List

import grpc

from xionpy.client.networks import NetworkConfig
from xionpy.protos.cosmos.gov.v1.query_pb2 import QueryProposalsRequest
from xionpy.protos.cosmos.gov.v1.query_pb2_grpc import QueryStub as GovGrpcClient
from xionpy.services.controller import XionBaseController
from xionpy.services.gov.model import Proposal
from xionpy.services.gov.rest import GovRestClient


class XionGovController(XionBaseController):

    def __init__(self, cfg: NetworkConfig):
        super().__init__(cfg)
        if isinstance(self.binding, grpc.Channel):
            self.client = GovGrpcClient(self.binding)
        else:
            self.client = GovRestClient(self.binding)

    def query_proposals(self) -> List[Proposal]:
        req = QueryProposalsRequest()
        resp = self.client.Proposals(req)

        proposals: List[Proposal] = []
        for proposal in resp.proposals:
            proposals.append(
                Proposal.from_proto(proposal)
            )
        return proposals
