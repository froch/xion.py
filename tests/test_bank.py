from xionpy.client import XionClient
from xionpy.client.config import NetworkConfig
from xionpy.client.wallet import XionWallet
from xionpy.mnemonic import generate_mnemonic
import os

def test_bank_balance():
    m = os.getenv("XION_MNEMONIC", generate_mnemonic())
    wallet = XionWallet.from_mnemonic(m)
    client = XionClient(NetworkConfig.localhost())

    balance = client.query_bank_balance(wallet.address())
