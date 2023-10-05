from web3 import Web3

new_key = Web3().eth.account.create()
print(f'Wallet address is:  {new_key.address}')
print(f'Private key is:  {new_key.key.hex()}')
