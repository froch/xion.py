from xionpy.services.base.tendermint.models import (
    GetBlockByHeightResponseModel,
    GetLatestBlockResponseModel,
    GetLatestValidatorSetResponseModel,
    GetNodeInfoResponseModel,
    GetSyncingResponseModel,
    GetValidatorSetByHeightResponseModel,
)


def test_get_node_info(xion):
    response = xion.tendermint.query_node_info()
    assert response is not None
    assert isinstance(response, GetNodeInfoResponseModel)
    assert response.default_node_info is not None


def test_get_syncing(xion):
    response = xion.tendermint.query_syncing()
    assert response is not None
    assert isinstance(response, GetSyncingResponseModel)
    assert isinstance(response.syncing, bool)


def test_get_latest_block(xion):
    r = xion.tendermint.query_latest_block()
    assert r is not None
    assert isinstance(r, GetLatestBlockResponseModel)
    assert r.block is not None
    assert r.block_id is not None
    assert r.sdk_block is not None


def test_get_block_by_height(xion):
    latest_block = xion.tendermint.query_latest_block()
    height = latest_block.block.header.height
    expected_hash = latest_block.block_id.hash
    r = xion.tendermint.query_block_by_height(height=height)
    assert r is not None
    assert isinstance(r, GetBlockByHeightResponseModel)
    assert r.block is not None
    assert r.block.header.height == height
    assert r.block_id is not None
    assert r.block_id.hash == expected_hash


def test_get_latest_validator_set(xion):
    response = xion.tendermint.query_latest_validator_set()
    assert response is not None
    assert isinstance(response, GetLatestValidatorSetResponseModel)
    assert response.validators is not None
    assert len(response.validators) >= 0


def test_get_validator_set_by_height(xion):
    latest_block = xion.tendermint.query_latest_block()
    height = latest_block.block.header.height
    response = xion.tendermint.query_validators_by_height(height=height)
    assert response is not None
    assert isinstance(response, GetValidatorSetByHeightResponseModel)
    assert response.validators is not None
    assert len(response.validators) > 0
