#!/usr/bin/env python3


import os
import sys
import subprocess
import shutil

# Define the new file from the command line.

# run MD5 on new file with subprocess
def load_md5(new_file):
	if shutil.which('md5sum'):
		md5 = subprocess.run(["md5sum",new_file], stdout=subprocess.PIPE )
		stdout = md5.stdout
		stdout = stdout.split()
		stdout = stdout[0]
		stdout = stdout.decode("utf-8")
	elif shutil.which("md5"):
		md5 = subprocess.run(["md5",new_file], stdout=subprocess.PIPE )
		stdout = md5.stdout
		stdout = stdout.split()
		stdout = stdout[3]
		stdout = stdout.decode("utf-8")
	else:
		raise OSError('no md5 or md5sum in path')

	return stdout


if __name__ == '__main__':
	new_file = sys.argv[1]
	print(load_md5(new_file))



