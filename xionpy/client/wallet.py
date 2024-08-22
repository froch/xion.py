from abc import ABC, abstractmethod
from collections import UserString
from typing import Optional

from xionpy.crypto.address import Address
from xionpy.crypto.hashfuncs import sha256
from xionpy.crypto.interface import Signer
from xionpy.services.crypto.secp256k1.model import PrivateKey, PublicKey
from xionpy.crypto.mnemonic import COSMOS_HD_PATH, derive_child_key_from_mnemonic


class Wallet(ABC, UserString):

    @abstractmethod
    def address(self) -> Address:
        """get the address of the wallet.

        :return: None
        """

    @abstractmethod
    def public_key(self) -> PublicKey:
        """get the public key of the wallet.

        :return: None
        """

    @abstractmethod
    def signer(self) -> Signer:
        """get the signer of the wallet.

        :return: None
        """

    @property
    def data(self):
        """Get the address of the wallet.

        :return: Address
        """
        return self.address()

    def __json__(self):
        """
        Return the address in string format.

        :return: address in string format
        """
        return str(self.address())


class XionWallet(Wallet):

    @staticmethod
    def generate(prefix: Optional[str] = None) -> "XionWallet":
        return XionWallet(PrivateKey(), prefix=prefix)

    @staticmethod
    def from_mnemonic(mnemonic: str, prefix: Optional[str] = None) -> "XionWallet":
        child_key = derive_child_key_from_mnemonic(mnemonic, path=COSMOS_HD_PATH)
        return XionWallet(PrivateKey(child_key), prefix=prefix)

    @staticmethod
    def from_unsafe_seed(
        text: str, index: Optional[int] = None, prefix: Optional[str] = None
    ) -> "XionWallet":
        private_key_bytes = sha256(text.encode())
        if index is not None:
            private_key_bytes = sha256(
                private_key_bytes + index.to_bytes(4, byteorder="big")
            )
        return XionWallet(PrivateKey(private_key_bytes), prefix=prefix)

    def __init__(self, private_key: PrivateKey, prefix: Optional[str] = None):
        self._private_key = private_key
        self._public_key = private_key.public_key
        self._prefix = prefix

    def address(self) -> Address:
        return Address(self._public_key, self._prefix)

    def public_key(self) -> PublicKey:
        return self._public_key

    def signer(self) -> PrivateKey:
        return self._private_key
