import json
import settings

# Read from file
with open(settings.CONTRACT_JSON_FILENAME, 'r') as f:
    json_file = json.load(f)

# Export ABI and bytecode
abi = json_file[settings.CONTRACT_PATH]['abi']
bytecode = json_file[settings.CONTRACT_PATH]['bin']
