import wget
import os, sys
pid = sys.argv[1]

wget.download(f"http://ulif.neocities.org/uligne/packages/{pid}/src/{pid}.ugn", f"{pid}.ugn")
os.system(f'mv {pid}.ugn ~/.local/lib/uligne/cache/')
os.system(f'unzip ~/.local/lib/uligne/cache/{pid}.ugn')
os.system(f'rm ~/.local/lib/uligne/cache/{pid}.ugn')
os.system(f'mv ~/.local/lib/uligne/cache/{pid} ~/Documents/Applications/')
print(f'Installed {pid}')
