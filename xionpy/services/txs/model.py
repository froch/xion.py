import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from google.protobuf.any_pb2 import Any as ProtoAny

from xionpy.client.coins import parse_coins
from xionpy.client.exceptions import (
    BroadcastError,
    InsufficientFeesError,
    InvalidSigningModeError,
    NotFoundError,
    OutOfGasError,
)
from xionpy.crypto.address import Address
from xionpy.crypto.interface import Signer
from xionpy.crypto.keypairs import PublicKey
from xionpy.protos.cosmos.crypto.secp256k1.keys_pb2 import PubKey as ProtoPubKey
from xionpy.protos.cosmos.tx.signing.v1beta1.signing_pb2 import SignMode
from xionpy.protos.cosmos.tx.v1beta1.tx_pb2 import (
    AuthInfo,
    Fee,
    ModeInfo,
    SignDoc,
    SignerInfo,
    Tx,
    TxBody,
)


class TxState(Enum):
    Draft = 0
    Sealed = 1
    Final = 2


def _is_iterable(value) -> bool:
    try:
        iter(value)
        return True
    except TypeError:
        return False


def _wrap_in_proto_any(values: List[Any]) -> List[ProtoAny]:
    any_values = []
    for value in values:
        proto_any = ProtoAny()
        proto_any.Pack(value, type_url_prefix="/")  # type: ignore
        any_values.append(proto_any)
    return any_values


def _create_proto_public_key(public_key: PublicKey) -> ProtoAny:
    proto_public_key = ProtoAny()
    proto_public_key.Pack(
        ProtoPubKey(
            key=public_key.public_key_bytes,
        ),
        type_url_prefix="/",
    )
    return proto_public_key


class SigningMode(Enum):
    Direct = 1


@dataclass
class SigningCfg:

    mode: SigningMode
    sequence_num: int
    public_key: PublicKey

    @staticmethod
    def direct(public_key: PublicKey, sequence_num: int) -> "SigningCfg":
        return SigningCfg(
            mode=SigningMode.Direct,
            sequence_num=sequence_num,
            public_key=public_key,
        )


class Transaction:
    def __init__(self):
        self._msgs: List[Any] = []
        self._state: TxState = TxState.Draft
        self._tx_body: Optional[TxBody] = None
        self._tx = None
        self._fee = None

    @property  # noqa
    def state(self) -> TxState:
        return self._state

    @property  # noqa
    def msgs(self):
        return self._msgs

    @property
    def fee(self) -> Optional[str]:
        return self._fee

    @property
    def tx(self):
        if self._state != TxState.Final:
            raise RuntimeError("The transaction has not been completed")
        return self._tx

    def add_message(self, msg: Any) -> "Transaction":
        if self._state != TxState.Draft:
            raise RuntimeError(
                "The transaction is not in the draft state. No further messages may be appended"
            )
        self._msgs.append(msg)
        return self

    def seal(
        self,
        signing_cfgs: Union[SigningCfg, List[SigningCfg]],
        fee: str,
        gas_limit: int,
        memo: Optional[str] = None,
    ) -> "Transaction":
        self._state = TxState.Sealed

        input_signing_cfgs: List[SigningCfg] = (
            signing_cfgs if _is_iterable(signing_cfgs) else [signing_cfgs]  # type: ignore
        )

        signer_infos = []
        for signing_cfg in input_signing_cfgs:
            if signing_cfg.mode != SigningMode.Direct:
                raise InvalidSigningModeError(signing_cfg.mode)

            signer_infos.append(
                SignerInfo(
                    public_key=_create_proto_public_key(signing_cfg.public_key),
                    mode_info=ModeInfo(
                        single=ModeInfo.Single(mode=SignMode.SIGN_MODE_DIRECT)
                    ),
                    sequence=signing_cfg.sequence_num,
                )
            )

        auth_info = AuthInfo(
            signer_infos=signer_infos,
            fee=Fee(amount=parse_coins(fee), gas_limit=gas_limit),
        )

        self._fee = fee

        self._tx_body = TxBody()
        self._tx_body.memo = memo or ""
        self._tx_body.messages.extend(
            _wrap_in_proto_any(self._msgs)
        )  # pylint: disable=E1101

        self._tx = Tx(body=self._tx_body, auth_info=auth_info)
        return self

    def sign(
        self,
        signer: Signer,
        chain_id: str,
        account_number: int,
        deterministic: bool = False,
    ) -> "Transaction":
        if self.state != TxState.Sealed:
            raise RuntimeError(
                "Transaction is not sealed. It must be sealed before signing is possible."
            )

        sd = SignDoc()
        sd.body_bytes = self._tx.body.SerializeToString()
        sd.auth_info_bytes = self._tx.auth_info.SerializeToString()
        sd.chain_id = chain_id
        sd.account_number = account_number

        data_for_signing = sd.SerializeToString()

        # Generating deterministic signature:
        signature = signer.sign(
            data_for_signing,
            deterministic=deterministic,
            canonicalise=True,
        )
        self._tx.signatures.extend([signature])
        return self

    def complete(self) -> "Transaction":
        self._state = TxState.Final
        return self

@dataclass
class MessageLog:
    """Message Log."""

    index: int  # noqa
    log: str  # noqa
    events: Dict[str, Dict[str, str]]


@dataclass
class TxResponse:
    """Transaction response.

    :raises OutOfGasError: Out of gas error
    :raises InsufficientFeesError: Insufficient fees
    :raises BroadcastError: Broadcast Exception
    """

    hash: str
    height: int
    code: int
    gas_wanted: int
    gas_used: int
    raw_log: str
    logs: List[MessageLog]
    events: Dict[str, Dict[str, str]]
    timestamp: Optional[datetime]

    def is_successful(self) -> bool:
        """Check transaction is successful.

        :return: transaction status
        """
        return self.code == 0

    def ensure_successful(self):
        """Ensure transaction is successful.

        :raises OutOfGasError: Out of gas error
        :raises InsufficientFeesError: Insufficient fees
        :raises BroadcastError: Broadcast Exception
        """
        if self.code != 0:

            if "out of gas" in self.raw_log:
                match = re.search(
                    r"gasWanted:\s*(\d+).*?gasUsed:\s*(\d+)", self.raw_log
                )
                if match is not None:
                    gas_wanted = int(match.group(1))
                    gas_used = int(match.group(2))
                else:
                    gas_wanted = -1
                    gas_used = -1
                raise OutOfGasError(self.hash, gas_wanted=gas_wanted, gas_used=gas_used)

            if "insufficient fees" in self.raw_log:
                match = re.search(r"required:\s*(\d+\w+)", self.raw_log)
                if match is not None:
                    required_fee = match.group(1)
                else:
                    required_fee = f"more than {self.gas_wanted}"
                raise InsufficientFeesError(self.hash, required_fee)

            raise BroadcastError(self.hash, self.raw_log)


class SubmittedTx:
    """Submitted transaction."""

    def __init__(
            self, client: "LedgerClient", tx_hash: str  # type: ignore # noqa: F821
    ):
        """Init the Submitted transaction.

        :param client: Ledger client
        :param tx_hash: transaction hash
        """
        self._client = client
        self._response: Optional[TxResponse] = None
        self._tx_hash = str(tx_hash)

    @property
    def tx_hash(self) -> str:
        """Get the transaction hash.

        :return: transaction hash
        """
        return self._tx_hash

    @property
    def response(self) -> Optional[TxResponse]:
        """Get the transaction response.

        :return: response
        """
        return self._response

    @property
    def contract_code_id(self) -> Optional[int]:
        """Get the contract code id.

        :return: return contract code id if exist else None
        """
        if self._response is None:
            return None

        code_id = self._response.events.get("store_code", {}).get("code_id")
        if code_id is None:
            return None

        return int(code_id)

    @property
    def contract_address(self) -> Optional[Address]:
        """Get the contract address.

        :return: return contract address if exist else None
        """
        if self._response is None:
            return None

        contract_address = self._response.events.get("instantiate", {}).get(
            "_contract_address"
        )
        if contract_address is None:
            return None

        return Address(contract_address)

    def wait_to_complete(
            self,
            timeout: Optional[Union[int, float, timedelta]] = None,
            poll_period: Optional[Union[int, float, timedelta]] = None,
    ) -> "SubmittedTx":
        """Wait to complete the transaction.

        :param timeout: timeout, defaults to None
        :param poll_period: poll_period, defaults to None

        :return: Submitted Transaction
        """
        self._response = self._client.wait_for_query_tx(
            self.tx_hash, timeout=timeout, poll_period=poll_period
        )

        if self._response is None:
            raise NotFoundError(self.tx_hash)
        self._response.ensure_successful()

        return self
