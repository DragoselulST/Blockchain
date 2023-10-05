# 1. Add imports
import random
import time

import settings
from contract import abi
from web3 import Web3


def main():
    # 2. Create Web3 instance
    web3 = Web3(Web3.HTTPProvider(settings.RPC_ENDPOINT))

    # 3. Create variables
    contract_address = settings.CONTRACT_ADDRESS

    # 4. Create contract instance
    IoTDevice = web3.eth.contract(address=contract_address, abi=abi)

    while True:
        # Simulate device read
        temperature = str(round(random.uniform(18, 32), 2))
        humidity = str(round(random.uniform(30, 70), 2))

        print("Temperature is {} and humidity is {}".format(temperature, humidity))

        # 5. Build addMeasurement tx
        add_massurement_tx = IoTDevice.functions.addMeassurement(temperature, humidity).build_transaction(
            {
                'from': settings.ACCOUNT_ADDRESS,
                'nonce': web3.eth.get_transaction_count(settings.ACCOUNT_ADDRESS),
            }
        )

        # 6. Sign tx with PK
        signed_tx = web3.eth.account.sign_transaction(add_massurement_tx, settings.ACCOUNT_PRIVATE)

        # 7. Send tx and wait for receipt
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # 8. Wait for receipt
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Tx successful with hash: {tx_receipt.transactionHash.hex()}')
        print(f'Gas used: {tx_receipt.gasUsed}')

        # 9. Wait 10 seconds
        print('Now we wait 10 seconds...')
        time.sleep(10)


if __name__ == '__main__':
    main()
