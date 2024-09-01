from xionpy.services.base.coin.models import CoinModel
from xionpy.services.base.tendermint.models import HeaderModel
from xionpy.services.staking.models import (
    DelegationModel,
    DelegationResponseModel,
    QueryHistoricalInfoResponseModel,
    QueryParamsResponseModel,
    QueryPoolResponseModel,
    QueryValidatorDelegationsResponseModel,
    QueryValidatorUnbondingDelegationsResponseModel,
    RedelegationResponseModel,
    ValidatorModel,
)


def test_query_validator(xion, nakanodo):
    expected = str(nakanodo)
    r = xion.staking.query_validator(expected)
    assert isinstance(r, ValidatorModel)
    assert r.operator_address == expected


def test_query_validators(xion):
    r = xion.staking.query_validators()
    assert isinstance(r, list)
    assert len(r) >= 0
    assert all(isinstance(validator, ValidatorModel) for validator in r)


def test_query_validator_by_moniker(xion):
    moniker = "nakanodo"
    r = xion.staking.query_validator_by_moniker(moniker)
    assert isinstance(r, ValidatorModel)
    assert moniker in r.description.moniker


def test_query_delegation(xion, nakanodo):
    delegator_addr = xion.wallet.address()
    r = xion.staking.query_delegation(delegator_addr, nakanodo)
    assert isinstance(r, DelegationResponseModel)
    assert r.delegation is not None
    assert r.balance is not None
    assert isinstance(r.balance, CoinModel)
    assert isinstance(r.delegation, DelegationModel)
    assert r.delegation.delegator_address == delegator_addr
    assert r.delegation.shares >= 0


def test_query_delegator_delegations(xion):
    delegator_addr = xion.wallet.address()
    r = xion.staking.query_delegator_delegations(delegator_addr)
    assert isinstance(r, list)
    assert len(r) >= 0
    assert all(isinstance(delegation, DelegationResponseModel) for delegation in r)


def test_query_delegator_unbonding_delegations(xion):
    delegator_addr = xion.wallet.address()
    r = xion.staking.query_delegator_unbonding_delegations(delegator_addr)
    assert isinstance(r, list)
    assert len(r) >= 0
    assert all(isinstance(unbonding, DelegationModel) for unbonding in r)


def test_query_redelegations(xion):
    delegator_addr = xion.wallet.address()
    r = xion.staking.query_redelegations(delegator_addr)
    assert isinstance(r, list)
    assert len(r) >= 0
    assert all(isinstance(rd, RedelegationResponseModel) for rd in r)


def test_query_historical_info(xion):
    height = 9650352
    r = xion.staking.query_historical_info(height)
    assert isinstance(r, QueryHistoricalInfoResponseModel)
    assert r.header is not None
    assert isinstance(r.header, HeaderModel)
    assert r.header.height == height


def test_query_pool(xion_client):
    result = xion_client.staking.query_pool()
    assert isinstance(result, QueryPoolResponseModel)
    assert result.pool.bonded_tokens is not None


def test_query_params(xion_client):
    result = xion_client.staking.query_params()
    assert isinstance(result, QueryParamsResponseModel)
    assert result.params.max_validators > 0


def test_query_validator_delegations(xion_client):
    validator_addr = "xionvaloper1nc8krpxkj6q3grxvs9ucskfq9rkts9v987h6xy"
    result = xion_client.staking.query_validator_delegations(validator_addr)
    assert isinstance(result, QueryValidatorDelegationsResponseModel)
    assert len(result.delegation_responses) > 0


def test_query_validator_unbonding_delegations(xion_client):
    validator_addr = "xionvaloper1nc8krpxkj6q3grxvs9ucskfq9rkts9v987h6xy"
    result = xion_client.staking.query_validator_unbonding_delegations(validator_addr)
    assert isinstance(result, QueryValidatorUnbondingDelegationsResponseModel)
    assert len(result.unbonding_responses) > 0
