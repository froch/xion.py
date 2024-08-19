from typing import Optional

from xionpy.client.networks import NetworkConfig
from xionpy.client.wallet import Wallet
from xionpy.crypto.address import Address
from xionpy.services.auth.controller import XionAuthController
from xionpy.services.bank.controller import XionBankController
from xionpy.services.txs.controller import XionTxsController
from xionpy.services.txs.gas import GasStrategy, SimulationGasStrategy
from xionpy.services.txs.model import SigningCfg, SubmittedTx, TxResponse


class XionClient:

    def __init__(
            self,
            cfg: NetworkConfig,
    ):
        cfg.validate()

        self.cfg = cfg
        self.gas_strategy: GasStrategy = SimulationGasStrategy(self)

        self.auth = XionAuthController(cfg)
        self.bank = XionBankController(cfg)
        self.txs = XionTxsController(cfg, self.gas_strategy)

    def tx_bank_send(
            self,
            sender: Wallet,
            recipient: Address,
            amount: int,
            denom: str,
            memo: Optional[str] = None,
    ) -> TxResponse:

        tx = self.bank.tx_send(
            sender=sender.address(),
            recipient=recipient,
            amount=amount,
            denom=denom,
        )

        submitted_tx = self.submit(
            tx=tx,
            sender=sender,
            memo=memo,
        )

        return self.txs.wait_for_tx(submitted_tx.tx_hash)

    def submit(
            self,
            tx: "Transaction",  # type: ignore # noqa: F821
            sender: "Wallet",  # type: ignore # noqa: F821
            account: Optional["Account"] = None,  # type: ignore # noqa: F821
            gas_limit: Optional[int] = None,
            memo: Optional[str] = None,
    ) -> SubmittedTx:

        if account is None:
            account = self.auth.query_account(sender.address())

        # estimate the fee for a provided gas limit
        if gas_limit is not None:
            fee = self.txs.estimate_fee_from_gas(gas_limit)

        # simulate the gas and fee for the transaction
        else:
            fee = f"{self.cfg.min_fee}{self.cfg.denom_fee}"
            tx.seal(
                SigningCfg.direct(sender.public_key(), account.sequence),
                fee=fee,
                gas_limit=self.gas_strategy.block_gas_limit(),
                memo=memo,
            )
            tx.sign(sender.signer(), self.cfg.chain_id, account.number)
            tx.complete()

            gas_limit, fee = self.txs.estimate_gas_and_fee(tx)

        # build the final transaction
        tx.seal(
            SigningCfg.direct(sender.public_key(), account.sequence),
            fee=fee,
            gas_limit=gas_limit,
            memo=memo,
        )
        tx.sign(sender.signer(), self.cfg.chain_id, account.number)
        tx.complete()

        return self.txs.broadcast(tx)
