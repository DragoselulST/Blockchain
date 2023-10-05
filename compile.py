# 1. Import solcx
import json

import solcx

import settings

if __name__ == '__main__':
    # 1. If you haven't already installed the Solidity compiler, uncomment the following line
    # solcx.install_solc('0.8.19')

    # 2. Compile contract
    temp_file = solcx.compile_files(
        'IoTDevice.sol',
        output_values=['abi', 'bin'],
        solc_version='0.8.19'
    )

    # Save the result
    with open(settings.CONTRACT_JSON_FILENAME, 'w') as f:
        json.dump(temp_file, f, indent=2)

    print('Compilation result saved as {}'.format(settings.CONTRACT_JSON_FILENAME))
