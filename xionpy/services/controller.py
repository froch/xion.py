
import certifi
import grpc

from xionpy.client.networks import NetworkConfig
from xionpy.client.urls import Protocol, parse_url
from xionpy.services.rest import XionBaseRestClient


class XionBaseController:

    def __init__(
            self,
             cfg: NetworkConfig = NetworkConfig.localhost(),
    ):

        self.cfg = cfg
        parsed_url = parse_url(self.cfg.url)

        if parsed_url.protocol == Protocol.GRPC:
            if parsed_url.secure:
                with open(certifi.where(), "rb") as f:
                    trusted_certs = f.read()
                credentials = grpc.ssl_channel_credentials(
                    root_certificates=trusted_certs
                )
                self.binding = grpc.secure_channel(parsed_url.host_and_port, credentials)
            else:
                self.binding = grpc.insecure_channel(parsed_url.host_and_port)
        else:
            self.binding = XionBaseRestClient(parsed_url.rest_url)
