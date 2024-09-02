from xionpy.services.base.coin.models import CoinModel
from xionpy.services.base.tendermint.models import HeaderModel
from xionpy.services.staking.models import (
    DelegationModel,
    DelegationResponseModel,
    ParamsModel,
    PoolModel,
    QueryHistoricalInfoResponseModel,
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
    latest_block = xion.tendermint.query_latest_block()
    height = latest_block.block.header.height
    r = xion.staking.query_historical_info(height=height)

    assert isinstance(r, QueryHistoricalInfoResponseModel)
    assert r.header is not None
    assert isinstance(r.header, HeaderModel)
    assert r.header.height == height
    assert r.valset is not None
    assert isinstance(r.valset, list)
    assert all(isinstance(validator, ValidatorModel) for validator in r.valset)
    assert len(r.valset) >= 0


def test_query_pool(xion):
    r = xion.staking.query_pool()

    assert isinstance(r, PoolModel)
    assert r.bonded_tokens is not None
    assert isinstance(r.bonded_tokens, int)
    assert r.bonded_tokens >= 0
    assert r.not_bonded_tokens is not None
    assert isinstance(r.not_bonded_tokens, int)
    assert r.not_bonded_tokens >= 0


def test_query_params(xion):
    r = xion.staking.query_params()

    assert isinstance(r, ParamsModel)
    assert r is not None
    assert r.bond_denom is not None
    assert r.historical_entries > 0
    assert r.max_entries > 0
    assert r.max_validators > 0
    assert r.min_commission_rate is not None


def test_query_validator_delegations(xion, nakanodo):
    r = xion.staking.query_validator_delegations(
        validator_addr=nakanodo,
    )

    assert isinstance(r, QueryValidatorDelegationsResponseModel)
    assert isinstance(r.delegation_responses, list)
    assert len(r.delegation_responses) >= 0
    assert all(isinstance(delegation, DelegationResponseModel) for delegation in r.delegation_responses)

def test_query_validator_unbonding_delegations(xion, nakanodo):
    result = xion.staking.query_validator_unbonding_delegations(nakanodo)

    assert isinstance(result, QueryValidatorUnbondingDelegationsResponseModel)
    assert len(result.unbonding_responses) > 0
