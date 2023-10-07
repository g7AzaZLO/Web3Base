import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

ABIS_DIR = os.path.join(ROOT_DIR, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')

private_key = ""
seed = ""
ETH_RPC = "https://eth.llamarpc.com"
BSC_PRC = "https://binance.llamarpc.com"
POLYGON_PRC = "https://polygon.llamarpc.com"
AVALANCHE_PRC = "https://avalanche.public-rpc.com"
ARBITRUM_PRC = "https://arbitrum.llamarpc.com"
OPTIMISM_PRC = "https://optimism.llamarpc.com"
FANTOM_PRC = "https://fantom.publicnode.com"
BASE_PRC = "https://endpoints.omniatech.io/v1/base/mainnet/public"
AURORA_PRC = "https://endpoints.omniatech.io/v1/aurora/mainnet/public"
LINEA_PRC = "https://1rpc.io/linea"

USDT_PRICE_URL = "https://api.coinbase.com/v2/exchange-rates?currency="
