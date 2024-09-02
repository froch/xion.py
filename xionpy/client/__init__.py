from xionpy.client.networks import NetworkConfig
from xionpy.client.wallet import XionWallet
from xionpy.services.auth.controller import XionAuthController
from xionpy.services.bank.controller import XionBankController
from xionpy.services.base.tendermint.controller import XionTendermintController
from xionpy.services.gov.controller import XionGovController
from xionpy.services.staking.controller import XionStakingController
from xionpy.services.txs.controller import XionTxsController
from xionpy.services.txs.gas import GasStrategy, SimulationGasStrategy


class XionClient:

    def __init__(
            self,
            cfg: NetworkConfig = None,
            wallet: XionWallet = None,
    ):
        """
        Initialize a new XionClient.
        :param cfg: NetworkConfig
        :param wallet: XionWallet
        """

        if cfg is None:
            cfg = NetworkConfig.xion_testnet_1()

        if wallet is None:
            wallet = XionWallet.generate()

        cfg.validate()

        self.cfg = cfg
        self.wallet = wallet

        self.gas_strategy: GasStrategy = SimulationGasStrategy(self)

        self.auth = XionAuthController(cfg, wallet)
        self.bank = XionBankController(cfg, wallet)
        self.gov = XionGovController(cfg, wallet)
        self.staking = XionStakingController(cfg, wallet)
        self.tendermint = XionTendermintController(cfg)

        self.txs = XionTxsController(cfg, wallet, self.gas_strategy, self.auth)
