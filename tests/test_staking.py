import os

from xionpy.client import XionClient
from xionpy.client.networks import NetworkConfig
from xionpy.client.wallet import XionWallet
from xionpy.crypto.address import Address
from xionpy.crypto.mnemonic import generate_mnemonic
from xionpy.services.txs.model import TxResponse


def test_staking_query_validators():
    xion = XionClient(cfg=NetworkConfig.localhost())
    validators = xion.staking.query_validators()
    assert validators is not None
    assert isinstance(validators, list)
    assert len(validators) > 0


def test_query_validator_by_moniker():
    xion = XionClient(cfg=NetworkConfig.localhost())
    moniker = "ahi"
    validator = xion.staking.query_validator_by_moniker("ahi")
    assert validator is not None
    assert moniker in validator.moniker


def test_query_validator_by_address():
    xion = XionClient(cfg=NetworkConfig.localhost())
    moniker = "ahi"
    validator = xion.staking.query_validator_by_moniker(moniker)
    address = str(validator.address)
    validator = xion.staking.query_validator_by_address(address)
    assert validator is not None
    assert validator.address == address


def test_staking_tx_delegate():
    m = os.getenv("XION_MNEMONIC", generate_mnemonic())
    wallet = XionWallet.from_mnemonic(m)
    nakanodo = Address("xionvaloper1nc8krpxkj6q3grxvs9ucskfq9rkts9v987h6xy")

    network = NetworkConfig.localhost()
    xion = XionClient(network)
    amount = 1_000_000

    draft_tx = xion.staking.tx_delegate(
        delegator=wallet.address(),
        validator=nakanodo,
        amount=amount,
        denom=network.denom_staking,
    )

    tx = xion.txs.submit(
        tx=draft_tx,
        sender=wallet,
    )

    assert tx is not None
    assert isinstance(tx, TxResponse)
    assert tx.hash is not None
    assert tx.code == 0
