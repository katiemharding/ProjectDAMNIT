#/usr/bin/env python3



import sys
import subprocess


# Define the new file from the command line.

# run MD5 on new file with subprocess
def load_md5(new_file):
	md5 = subprocess.run(["md5",new_file], stdout=subprocess.PIPE )
	stdout = md5.stdout
	stdout = stdout.split()
	stdout = stdout[3]
	stdout = stdout.decode("utf-8")
	return stdout

print(__name__)

if __name__ == '__main__':
	new_file = sys.argv[1]
	print(load_md5(new_file))


