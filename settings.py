ACCOUNT_ADDRESS = '' # Wallet address
ACCOUNT_PRIVATE = '' # Wallet private key

CONTRACT_ADDRESS = '' # Fill with the smart contract address once you deployed it (in step 3)

RPC_ENDPOINT = 'HTTP://127.0.0.1:7545' # The RPC endpoint of the network
CONTRACT_NAME = 'IoTDevice'

# DO NOT EDIT AFTER THIS LINE
CONTRACT_SOL_FILE = '{contract_name}.sol'.format(contract_name=CONTRACT_NAME)
CONTRACT_PATH = '{contract_name}.sol:{contract_name}'.format(contract_name=CONTRACT_NAME)
CONTRACT_JSON_FILENAME = '{contract_name}.json'.format(contract_name=CONTRACT_NAME)
