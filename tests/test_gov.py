from xionpy.client import XionClient
from xionpy.client.networks import NetworkConfig


def test_query_proposals():
    xion = XionClient(cfg=NetworkConfig.localhost())
    proposals = xion.gov.query_proposals()
    assert proposals is not None
    assert isinstance(proposals, list)
    assert len(proposals) > 0
