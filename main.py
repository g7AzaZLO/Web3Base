from cClient import *
from data.config import *

print("""
░██╗░░░░░░░██╗███████╗██████╗░██████╗░██████╗░░█████╗░░██████╗███████╗
░██║░░██╗░░██║██╔════╝██╔══██╗╚════██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
░╚██╗████╗██╔╝█████╗░░██████╦╝░█████╔╝██████╦╝███████║╚█████╗░█████╗░░
░░████╔═████║░██╔══╝░░██╔══██╗░╚═══██╗██╔══██╗██╔══██║░╚═══██╗██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██████╔╝██████╦╝██║░░██║██████╔╝███████╗  By
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═════╝░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝    [G7]AzaZLO""")


def native_checker() -> None:
    address = input("Enter your address: ")
    balance_eth = check_native_balance(address, ETH_RPC)
    balance_eth_usdt = round(balance_eth * check_price_in_usdt("ETH"), 4)
    print(f"Ethereum: {balance_eth:f} ETH | {balance_eth_usdt}$")

    balance_bnb = check_native_balance(address, BSC_PRC)
    balance_bnb_usdt = round(balance_bnb * check_price_in_usdt("BNB"), 4)
    print(f"BSC: {balance_bnb:f} BNB | {balance_bnb_usdt}$")

    balance_polygon = check_native_balance(address, POLYGON_PRC)
    balance_polygon_usdt = round(balance_polygon * check_price_in_usdt("MATIC"), 4)
    print(f"Polygon: {balance_polygon:f} MATIC | {balance_polygon_usdt}$")

    balance_avax = check_native_balance(address, AVALANCHE_PRC)
    balance_avax_usdt = round(balance_avax * check_price_in_usdt("AVAX"), 4)
    print(f"Avalanche: {balance_avax:f} AVAX | {balance_avax_usdt}$")

    balance_arb = check_native_balance(address, ARBITRUM_PRC)
    balance_arb_usdt = round(balance_arb * check_price_in_usdt("ETH"), 4)
    print(f"Arbitrum: {balance_arb:f} ETH | {balance_arb_usdt}$")

    balance_optimism = check_native_balance(address, OPTIMISM_PRC)
    balance_optimism_usdt = round(balance_optimism * check_price_in_usdt("ETH"), 4)
    print(f"Optimism: {balance_optimism:f} ETH | {balance_optimism_usdt}$")

    balance_fantom = check_native_balance(address, FANTOM_PRC)
    balance_fantom_usdt = round(balance_fantom * check_price_in_usdt("FTM"), 4)
    print(f"Fantom: {balance_fantom:f} FTM | {balance_fantom_usdt}$")

    balance_base = check_native_balance(address, BASE_PRC)
    balance_base_usdt = round(balance_base * check_price_in_usdt("ETH"), 4)
    print(f"Base: {balance_base:f} ETH | {balance_base_usdt}$")

    balance_aurora = check_native_balance(address, AURORA_PRC)
    balance_aurora_usdt = round(balance_aurora * check_price_in_usdt("ETH"), 4)
    print(f"Aurora: {balance_aurora:f} ETH | {balance_aurora_usdt}$")

    balance_linea = check_native_balance(address, LINEA_PRC)
    balance_linea_usdt = round(balance_linea * check_price_in_usdt("ETH"), 4)
    print(f"Linea: {balance_linea:f} ETH | {balance_linea_usdt}$")


if __name__ == '__main__':
    while True:
        print("\n")
        print("1) Checker of native balance")
        print("q) Exit")
        choise = input("-> ")
        if choise == "1":
            native_checker()
        elif choise == "q":
            exit()
        else:
            print("There's no such option")
