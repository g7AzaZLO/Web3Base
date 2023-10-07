import requests
from data.config import *
from web3 import Web3

from utils import read_json
from models import TokenAmount


class Client:
    #default_abi = read_json(TOKEN_ABI)

    def __init__(
            self,
            private_key: str,
            rpc: str
    ):
        self.private_key = private_key
        self.rpc = rpc
        self.w3 = Web3(Web3.HTTPProvider(endpoint_uri=self.rpc))
        self.address = Web3.to_checksum_address(self.w3.eth.account.from_key(private_key=private_key).address)

    # Получить количество нулей после запятой
    def get_decimals(self, contract_address: str):
        return int(self.w3.eth.contract(
            address=Web3.to_checksum_address(contract_address),
            abi=Client.default_abi
        ).functions.decimals().call())

    # Проверить баланс определенной монеты
    def balance_of(self, contract_address: str):
        return self.w3.eth.contract(
            address=Web3.to_checksum_address(contract_address),
            abi=Client.default_abi
        ).functions.balanceOf(self.address).call()

    # Дать апрув на списание такого-то токена такому-то контракту
    def get_allowance(self, token_address: str, spender: str):
        return self.w3.eth.contract(
            address=Web3.to_checksum_address(token_address),
            abi=Client.default_abi
        ).functions.allowance(self.address, spender).call()

    # Проверка наличия суммы на балансе
    def check_balance_on_min_value(self, token_address: str, min_value: int) -> bool:
        print(f"{self.address} | balaceOf | check balance of {token_address}")
        balance = self.balance_of(contract_address=token_address)
        decimal = self.get_decimals(contract_address=token_address)
        if balance < min_value * 10 ** decimal:
            print(f"{self.address} | balaceOf | not enough {token_address}")
            return False
        return True

    def send_transaction(
            self,
            to,
            data=None,
            from_=None,
            increase_gas=1.1,
            value=None
    ):
        if not from_:
            from_ = self.address
        tx_params = {
            'chainId': self.w3.eth.chain_id,
            'nonce': self.w3.eth.get_transaction_count(self.address),
            'from': Web3.to_checksum_address(from_),
            'to': Web3.to_checksum_address(to),
            'fasPrice': self.w3.eth.gas_price
        }
        if not data:
            tx_params['data'] = data
        if value:
            tx_params['value'] = value
        try:
            tx_params['gas'] = int(self.w3.eth.estimate_gas(tx_params) * increase_gas)
        except Exception as err:
            print(f"{self.address} | Transaction failed | {err}")
            return None
        sign = self.w3.eth.account.sign_transaction(tx_params, self.private_key)
        return self.w3.eth.send_raw_transaction(sign.rawTransaction)

    def check_tx(self, tx_hash) -> bool:
        try:
            data = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=200)
            if 'status' in data and data['status'] == 1:
                print(f"{self.address} | transaction was sucsessfull: {tx_hash.hex()}")
                return True
            else:
                print(f"{self.address} | transaction failed {data['transactionHash'].hex()}")
                return False
        except Exception as err:
            print(f"{self.address} | unexpected error in <check_tx> function: {err}")
            return False

    def approve(self, token_address: str, spender: str, amount: TokenAmount | None = None):
        contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(token_address),
            abi=Client.default_abi
        )
        return self.send_transaction(
            to=token_address,
            data=contract.encodeABI('approve',
                                    args=(
                                        spender,
                                        amount.Wei
                                    ))
        )

    def check_approve(self, token_address: str, spender: str, amount: TokenAmount | None = None) -> bool:
        print(f"{self.address} | approve | start approve {token_address} for spender {spender}")
        decimals = self.get_decimals(contract_address=token_address)
        balance = TokenAmount(
            amount=self.balance_of(contract_address=token_address),
            decimals=decimals,
            wei=True
        )
        if balance.Wei <= 0:
            print(f"{self.address} | approve | zero balance")
            return False
        if not amount or amount.Wei > balance.Wei:
            amount = balance
        approved = TokenAmount(
            amount=self.get_allowance(token_address=token_address, spender=spender),
            decimals=decimals,
            wei=True
        )
        if amount.Wei <= approved.Wei:
            print(f"{self.address} | approve | already approved")
            return True
        tx_hash = self.approve(token_address=token_address, spender=spender, amount=amount)
        if not self.check_tx(tx_hash=tx_hash):
            print(f"{self.address} | approve | {token_address} for spender {spender}")
            return False

def check_native_balance(address, rpc):
    web3 = Web3(Web3.HTTPProvider(rpc))
    address = Web3.to_checksum_address(address)
    balance = web3.eth.get_balance(address)
    ether_balance = Web3.from_wei(balance,"ether")
    return float(ether_balance)

def check_price_in_usdt(token):
    responce = requests.get(USDT_PRICE_URL+token)
    data = responce.json()
    price_in_usdt = data["data"]["rates"]["USD"]
    return float(price_in_usdt)

