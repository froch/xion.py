from dataclasses import dataclass
from typing import Optional, Union

from xionpy.client.exceptions import NetworkConfigError

URL_PREFIXES = (
    "grpc+https",
    "grpc+http",
    "rest+https",
    "rest+http",
)


@dataclass
class NetworkConfig:
    chain_id: str
    fee_minimum_gas_price: Union[int, float]
    fee_denomination: str
    staking_denomination: str
    url: str
    faucet_url: Optional[str] = None

    def validate(self):
        if self.chain_id == "":
            raise NetworkConfigError("No Chain ID is set")
        if self.url == "":
            raise NetworkConfigError("No RPC URL is set")
        if not any(
                map(
                    lambda x: self.url.startswith(x),
                    URL_PREFIXES,
                )
        ):
            prefix_list = ", ".join(map(lambda x: f'"{x}"', URL_PREFIXES))
            raise NetworkConfigError(
                f"URL must be one of: {prefix_list}"
            )

    @classmethod
    def localhost(cls) -> "NetworkConfig":
        return NetworkConfig(
            chain_id="xion-testnet-1",
            url="grpc+http://localhost:9090",
            fee_minimum_gas_price=0.025,
            fee_denomination="uxion",
            staking_denomination="uxion",
            faucet_url=None,
        )

    @classmethod
    def xion_testnet_1(cls) -> "NetworkConfig":
        return NetworkConfig(
            chain_id="xion-testnet-1",
            url="grpc+https://grpc.xion-testnet-1.burnt.com",
            fee_minimum_gas_price=0.025,
            fee_denomination="uxion",
            staking_denomination="uxion",
            faucet_url=None,
        )

    @classmethod
    def xion_mainnet_1(cls) -> "NetworkConfig":
        return NetworkConfig(
            chain_id="xion-mainnet-1",
            url="grpc+https://grpc.xion-mainnet-1.burnt.com",
            fee_minimum_gas_price=0.025,
            fee_denomination="uxion",
            staking_denomination="uxion",
            faucet_url=None,
        )
