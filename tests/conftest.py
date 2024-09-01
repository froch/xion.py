import os

import pytest

from xionpy.client.wallet import XionWallet
from xionpy.crypto.mnemonic import generate_mnemonic


@pytest.fixture(scope='session', autouse=True)
def load_env():
    from dotenv import load_dotenv
    load_dotenv()

@pytest.fixture(scope='function')
def xion():
    from xionpy.client import XionClient
    from xionpy.client.networks import NetworkConfig
    m = os.getenv("XION_MNEMONIC", generate_mnemonic())
    wallet = XionWallet.from_mnemonic(m)
    xion = XionClient(cfg=NetworkConfig.xion_testnet_1(), wallet=wallet)
    return xion
