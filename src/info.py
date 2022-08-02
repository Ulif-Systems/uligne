import json, wget
import os, sys
pid = sys.argv[1]

wget.download(f"http://ulif.neocities.org/uligne/packages/{pid}/package.json", "package.json")
with open('package.json') as f:
    j = json.load(f)
    name = j["pname"]
    type = j["issue"]
    id = j["id"]
    version = j["version"]
    os.system('clear')
    print(f'Package name: {name}')
    print(f'Package type: {type}')
    print(f'Package ID: {id}')
    print(f'Package version: {version}')
    os.system('rm package.json')
    input("Press ENTER to continue")
    os.system('clear')
