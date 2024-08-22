import math
import os
from abc import ABC, abstractmethod
from typing import Dict, Optional

from xionpy.services.txs.model import Transaction


class GasStrategy(ABC):
    """Transaction gas strategy."""

    @abstractmethod
    def estimate_gas(self, tx: Transaction) -> int:
        """Estimate the transaction gas.

        :param tx: Transaction
        :return: None
        """

    @abstractmethod
    def block_gas_limit(self) -> int:
        """Get the block gas limit.

        :return: None
        """

    def _clip_gas(self, value: int) -> int:
        block_limit = self.block_gas_limit()
        if block_limit < 0:
            return value
        return min(value, block_limit)


class SimulationGasStrategy(GasStrategy):
    DEFAULT_MULTIPLIER = os.getenv("XION_GAS_ADJUSTMENT", 1.4)
    DEFAULT_MARGIN = os.getenv("XION_GAS_ADJUSTMENT_MARGIN", 6000)

    def __init__(self, client: "XionClient", multiplier: Optional[float] = None):  # type: ignore # noqa: F821
        self.client = client
        self.max_gas: Optional[int] = None
        self.multiplier = multiplier or self.DEFAULT_MULTIPLIER

    def estimate_gas(self, tx: Transaction) -> int:
        gas_estimate = self.client.txs.simulate(tx) + self.DEFAULT_MARGIN
        gas_adjusted = math.ceil(gas_estimate * self.multiplier)
        return self._clip_gas(gas_adjusted)

    def block_gas_limit(self) -> int:
        if self.max_gas is None:
            # TODO(froch, 20240818): this subspace doesn't exist on XION
            # block_params = self._client.query_params("baseapp", "BlockParams")
            self.max_gas = 250_000
        return self.max_gas or -1


class OfflineMessageTableStrategy(GasStrategy):
    DEFAULT_FALLBACK_GAS_LIMIT = 250_000
    DEFAULT_BLOCK_LIMIT = 1_000_000

    @staticmethod
    def default_table() -> "OfflineMessageTableStrategy":
        strategy = OfflineMessageTableStrategy()
        strategy.update_entry("cosmos.bank.v1beta1.MsgSend", 100_000)
        strategy.update_entry("cosmwasm.wasm.v1.MsgStoreCode", 2_000_000)
        strategy.update_entry("cosmwasm.wasm.v1.MsgInstantiateContract", 250_000)
        strategy.update_entry("cosmwasm.wasm.v1.MsgExecuteContract", 400_000)
        return strategy

    def __init__(
            self,
            fallback_gas_limit: Optional[int] = None,
            block_limit: Optional[int] = None,
    ):
        self._table: Dict[str, int] = {}
        self._block_limit = block_limit or self.DEFAULT_BLOCK_LIMIT
        self._fallback_gas_limit = fallback_gas_limit or self.DEFAULT_FALLBACK_GAS_LIMIT

    def update_entry(self, transaction_type: str, gas_limit: int):
        self._table[str(transaction_type)] = int(gas_limit)

    def estimate_gas(self, tx: Transaction) -> int:
        gas_estimate = 0
        for msg in tx.msgs:
            gas_estimate += self._table.get(
                msg.DESCRIPTOR.full_name, self._fallback_gas_limit
            )
        return self._clip_gas(gas_estimate)

    def block_gas_limit(self) -> int:
        return self._block_limit
