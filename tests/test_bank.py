import os

from xionpy.client import XionClient, TxResponse
from xionpy.client.config import NetworkConfig
from xionpy.client.wallet import XionWallet
from xionpy.mnemonic import generate_mnemonic


def test_bank_balance():
    m = os.getenv("XION_MNEMONIC", generate_mnemonic())
    wallet = XionWallet.from_mnemonic(m)
    client = XionClient(NetworkConfig.localhost())

    balance = client.query_bank_balance(wallet.address())
    assert balance is not None
    assert isinstance(balance, int)
    assert balance >= 0

def test_bank_send():
    m = os.getenv("XION_MNEMONIC", generate_mnemonic())
    wallet = XionWallet.from_mnemonic(m)

    network = NetworkConfig.localhost()
    client = XionClient(network)

    amount = 1_000_000
    memo = "🔥 xion.py"
    tx = client.tx_bank_send(wallet.address(), amount, network.fee_denomination, wallet, memo)

    assert tx is not None
    assert isinstance(tx, TxResponse)
    assert tx.hash is not None
    assert tx.code == 0
