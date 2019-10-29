#!/usr/bin/env python3



from damnit_IO import read_json
import sys
import os.path
import json
from md5_module import load_md5

# Define imported file name
#new_file = sys.argv[1]

def status_damnit(new_file, damnit_path = '.damnit'):
	# Check if file exists
	if os.path.exists(new_file):
		print ('File is real')
	else:
		raise OSError('File is not real')

	# Convert new file into md5
	md5 = load_md5(new_file)


	# Open and read md5Graph_NewToOld.json file
	original_md5Graph = read_json(damnit_path + "/md5Graph_NewToOld.json")

	# Open and read filenames_dict.json file
	filenames_dict = read_json(damnit_path + "/filenames_dict.json")

	# Check if md5 exists in md5_dict.json file
	if md5 in original_md5Graph and md5 in filenames_dict.values() and new_file in filenames_dict:
		print('File exists in database')
		print(new_file)
	elif new_file in filenames_dict and md5 not in original_md5Graph:
		print('File needs to be updated.')
		print(new_file)
	elif md5 in original_md5Graph and new_file not in filenames_dict:
		print('File name has changed and needs updated.')
		print(new_file)
	else:
		print('File does not exist in database')
		print(new_file)

	return status_damnit


if __name__ == '__main__':

	new_file = sys.argv[1]

	status_damnit()





