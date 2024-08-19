import os

from xionpy.client import XionClient
from xionpy.client.networks import NetworkConfig
from xionpy.client.wallet import XionWallet
from xionpy.crypto.mnemonic import generate_mnemonic
from xionpy.services.txs.model import TxResponse


def test_bank_query_balances():
    m = os.getenv("XION_MNEMONIC", generate_mnemonic())
    wallet = XionWallet.from_mnemonic(m)
    xion = XionClient(cfg=NetworkConfig.localhost())

    balance = xion.bank.query_balances(wallet.address())
    assert balance is not None
    assert isinstance(balance, int)
    assert balance >= 0

def test_bank_send():
    m = os.getenv("XION_MNEMONIC", generate_mnemonic())
    wallet = XionWallet.from_mnemonic(m)

    network = NetworkConfig.localhost()
    xion = XionClient(network)

    amount = 1_000_000
    memo = "🔥 xion.py"
    tx = xion.tx_bank_send(
        wallet,
        wallet.address(),
        amount,
        network.denom_fee,
        memo,
    )

    assert tx is not None
    assert isinstance(tx, TxResponse)
    assert tx.hash is not None
    assert tx.code == 0
