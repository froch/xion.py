class NetworkConfigError(Exception):
    """Invalid Network Config."""


class NotFoundError(Exception):
    """Not found Error."""


class BroadcastError(Exception):
    """Broadcast Error."""

    def __init__(self, tx_hash: str, message: str):
        """Init Broadcast error.

        :param tx_hash: transaction hash
        :param message: message
        """
        super().__init__(message)
        self.tx_hash = tx_hash


class OutOfGasError(Exception):
    """Insufficient Fess Error."""

    def __init__(self, tx_hash: str, gas_wanted: int, gas_used: int):
        """Initialize.

        :param tx_hash: transaction hash
        :param gas_wanted: gas required to complete the transaction
        :param gas_used: gas used
        """
        self.gas_wanted = gas_wanted
        self.gas_used = gas_used
        super().__init__(
            tx_hash, f"Out of Gas (wanted: {self.gas_wanted}, used: {self.gas_used})"
        )


class InsufficientFeesError(Exception):
    """Insufficient Fess Error."""

    def __init__(self, tx_hash: str, minimum_required_fee: str):
        """Initialize.

        :param tx_hash: transaction hash
        :param minimum_required_fee: Minimum required fee
        """
        self.minimum_required_fee = minimum_required_fee
        super().__init__(
            tx_hash,
            f"Insufficient Fees (minimum required: {self.minimum_required_fee})",
        )


class InvalidSigningModeError(Exception):
    """Invalid Signing Mode Error."""

class InvalidDenominationError(Exception):
    """Invalid Denomination Error."""
