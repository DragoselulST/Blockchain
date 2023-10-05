# 1. Add imports
from web3 import Web3
import settings
from contract import abi, bytecode


def main():
    # 2. Add the Web3 provider logic here:
    web3 = Web3(Web3.HTTPProvider(settings.RPC_ENDPOINT))

    print(f'Attempting to deploy from account: {settings.ACCOUNT_ADDRESS}')

    # 3. Create contract instance
    IoTDevice = web3.eth.contract(abi=abi, bytecode=bytecode)

    # 4. Build constructor tx
    construct_tx = IoTDevice.constructor().build_transaction(
        {
            'from': settings.ACCOUNT_ADDRESS,
            'nonce': web3.eth.get_transaction_count(settings.ACCOUNT_ADDRESS),
        }
    )

    # 5. Sign tx with PK
    signed_tx = web3.eth.account.sign_transaction(construct_tx, settings.ACCOUNT_PRIVATE)

    # 6. Send tx
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # 7. Wait for the receipt of the tx
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    # 8. Print contract address
    print(f'Contract deployed at address: {tx_receipt.contractAddress}')
    print('YOU MIGHT WANT TO WRITE THIS DOWN!')


if __name__ == '__main__':
    main()
