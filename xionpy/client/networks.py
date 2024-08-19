import os
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
    denom_fee: str
    denom_staking: str
    faucet_url: Optional[str]
    min_fee: Union[int, float]
    url: str

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
            chain_id=os.getenv("XION_LOCALHOST_CHAIN_ID", "xion-testnet-1"),
            url=os.getenv("XION_LOCALHOST_RPC_URL", "grpc+http://localhost:9090"),
            min_fee=os.getenv("XION_LOCALHOST_MIN_FEE", 0.025),
            denom_fee=os.getenv("XION_LOCALHOST_DENOM_FEE", "uxion"),
            denom_staking=os.getenv("XION_LOCALHOST_DENOM_STAKING", "uxion"),
            faucet_url=os.getenv("XION_LOCALHOST_FAUCET_URL", None),
        )

    @classmethod
    def xion_testnet_1(cls) -> "NetworkConfig":
        return NetworkConfig(
            chain_id="xion-testnet-1",
            url="grpc+https://grpc.xion-testnet-1.burnt.com",
            min_fee=0.025,
            denom_fee="uxion",
            denom_staking="uxion",
            faucet_url=None,
        )

    @classmethod
    def xion_mainnet_1(cls) -> "NetworkConfig":
        return NetworkConfig(
            chain_id="xion-mainnet-1",
            url="grpc+https://grpc.xion-mainnet-1.burnt.com",
            min_fee=0.025,
            denom_fee="uxion",
            denom_staking="uxion",
            faucet_url=None,
        )
