from collections import UserString
from typing import Optional, Union

import bech32

from xionpy.crypto.hashfuncs import ripemd160, sha256
from xionpy.services.crypto.secp256k1.model import PublicKey


DEFAULT_PREFIX = "xion"


def _to_bech32(prefix: str, data: bytes) -> str:
    data_base5 = bech32.convertbits(data, 8, 5, True)
    if data_base5 is None:
        raise RuntimeError("Unable to parse address")  # pragma: no cover
    return bech32.bech32_encode(prefix, data_base5)


class Address(UserString):

    def __init__( # noqa
            self,
            value: Union[str, bytes, PublicKey, "Address"],
            prefix: Optional[str] = None,
    ):
        if prefix is None:
            prefix = DEFAULT_PREFIX

        if isinstance(value, str):
            _, data_base5 = bech32.bech32_decode(value)
            if data_base5 is None:
                raise RuntimeError("Unable to parse address")

            data_base8 = bech32.convertbits(data_base5, 5, 8, False)
            if data_base8 is None:
                raise RuntimeError("Unable to parse address")  # pragma: no cover

            self._address = bytes(data_base8)
            self._display = value

        elif isinstance(value, bytes):
            if len(value) != 20:
                raise RuntimeError("Incorrect address length")

            self._address = value
            self._display = _to_bech32(prefix, self._address)

        elif isinstance(value, PublicKey):
            self._address = ripemd160(sha256(value.public_key_bytes))
            self._display = _to_bech32(prefix, self._address)

        elif isinstance(value, Address):
            self._address = value._address
            # prefix might be different from the original Address, so we need to reencode it here.
            self._display = _to_bech32(prefix, self._address)
        else:
            raise TypeError("Unexpected type of `value` parameter")  # pragma: no cover

    def __str__(self):
        # noqa: D401
        return self._display

    def __bytes__(self):
        return self._address

    @property
    def data(self):  # noqa:
        return str(self)

    def __json__(self):  # noqa:
        return str(self)
