import settings
from web3 import Web3


def main():
    web3 = Web3(Web3.HTTPProvider(settings.RPC_ENDPOINT))
    balance = web3.from_wei(web3.eth.get_balance(settings.ACCOUNT_ADDRESS), 'ether')
    print(balance)


if __name__ == '__main__':
    main()
