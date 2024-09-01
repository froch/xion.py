from xionpy.services.bank.models import (
    CoinModel,
    DenomOwnerModel,
    MetadataModel,
    SendEnabledModel,
)


def test_bank_query_balances(xion):
    balance = xion.bank.query_balances()
    assert balance is not None
    assert isinstance(balance, int)
    assert balance >= 0


def test_bank_query_all_balances(xion):
    balances = xion.bank.query_all_balances()
    assert balances is not None
    assert isinstance(balances, list)
    assert all(isinstance(balance, CoinModel) for balance in balances)


def test_bank_query_denom_metadata(xion):
    denom = xion.cfg.denom_fee
    r = xion.bank.query_denom_metadata(denom)
    assert r is not None
    assert r.metadata.base == denom


def test_bank_query_denoms_metadata(xion):
    r = xion.bank.query_denoms_metadata()
    assert r is not None
    assert len(r.metadatas) > 0
    assert all(isinstance(metadata, MetadataModel) for metadata in r.metadatas)


def test_bank_query_total_supply(xion):
    r = xion.bank.query_total_supply()
    assert r is not None
    assert len(r.supply) > 0
    assert all(isinstance(coin, CoinModel) for coin in r.supply)


def test_bank_query_supply_of(xion):
    denom = xion.cfg.denom_fee
    r = xion.bank.query_supply_of(denom)
    assert r is not None
    assert r.amount is not None
    assert r.amount.denom == denom
    assert int(r.amount.amount) > 0


def test_bank_query_params(xion):
    r = xion.bank.query_params()
    assert r is not None
    assert r.params.default_send_enabled is True


def test_bank_query_spendable_balance_by_denom(xion):
    denom = xion.cfg.denom_fee
    r = xion.bank.query_spendable_balance_by_denom(denom=denom)
    assert r is not None
    assert r.balance is not None
    assert r.balance.denom == denom
    assert int(r.balance.amount) >= 0


def test_bank_query_spendable_balances(xion):
    r = xion.bank.query_spendable_balances()
    assert r is not None
    assert len(r.balances) > 0
    assert all(isinstance(balance, CoinModel) for balance in r.balances)


def test_bank_query_denom_owners(xion):
    denom = xion.cfg.denom_fee
    r = xion.bank.query_denom_owners(denom=denom)
    assert r is not None
    assert len(r.denom_owners) >= 0
    assert all(isinstance(owner, DenomOwnerModel) for owner in r.denom_owners)


def test_bank_query_send_enabled(xion):
    r = xion.bank.query_send_enabled()
    assert r is not None
    assert len(r.send_enabled) > 0
    assert all(isinstance(se, SendEnabledModel) for se in r.send_enabled)
