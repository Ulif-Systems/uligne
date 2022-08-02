import wget, os

if __name__ == "__main__":
	os.system("mkdir ~/.local/lib/uligne")
	os.system("mkdir ~/.local/lib/uligne/cache")
	os.system("cd ~/.local/lib/uligne")
	os.system("wget https://ulif.neocities.org/uligne/versions/1.0/info.py")
	os.system("wget https://ulif.neocities.org/uligne/versions/1.0/install.py")
	os.system("cd /usr/bin/")
	os.system("pkexec --user root wget https://ulif.neocities.org/uligne/versions/1.0/uligne")
	os.system("mkdir ~/Documents/Applications")
		
