from xionpy.client import XionClient
from xionpy.client.networks import NetworkConfig


def test_staking_query_validators():
    xion = XionClient(cfg=NetworkConfig.localhost())
    validators = xion.staking.query_validators()
    assert validators is not None
    assert isinstance(validators, list)
    assert len(validators) > 0
