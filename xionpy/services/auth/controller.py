import grpc

from xionpy.client.networks import NetworkConfig
from xionpy.crypto.address import Address
from xionpy.protos.cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from xionpy.protos.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest
from xionpy.protos.cosmos.auth.v1beta1.query_pb2_grpc import QueryStub as AuthGrpcClient
from xionpy.services.auth.model import Account
from xionpy.services.auth.rest import AuthRestClient
from xionpy.services.controller import XionBaseController


class XionAuthController(XionBaseController):

    def __init__(self, cfg: NetworkConfig):
        super().__init__(cfg)
        if isinstance(self.binding, grpc.Channel):
            self.client = AuthGrpcClient(self.binding)
        else:
            self.client = AuthRestClient(self.binding)

    def query_account(self, address: Address) -> Account:
        request = QueryAccountRequest(address=str(address))
        response = self.client.Account(request)

        account = BaseAccount()
        if not response.account.Is(BaseAccount.DESCRIPTOR):
            raise RuntimeError("Unexpected account type returned from query")
        response.account.Unpack(account)

        return Account(
            address=address,
            number=account.account_number,
            sequence=account.sequence,
        )
