

from xionpy.client.networks import NetworkConfig
from xionpy.services.auth.controller import XionAuthController
from xionpy.services.bank.controller import XionBankController
from xionpy.services.staking.controller import XionStakingController
from xionpy.services.txs.controller import XionTxsController
from xionpy.services.txs.gas import GasStrategy, SimulationGasStrategy


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
        self.staking = XionStakingController(cfg)
        self.txs = XionTxsController(cfg, self.gas_strategy, self.auth)
