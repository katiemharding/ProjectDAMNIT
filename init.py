#!/usr/bin/env python3

import subprocess
import os.path
import json
import glob
from md5_module import load_md5


def make_damnit():
	if os.path.exists('.damnit'):
		print('Folder exits')
	else:
		print('Folder does not exists')
		print('Making .damnit folder')
		os.mkdir('.damnit')

def all_file_name_dict():
	make_damnit()
	# Find all files in dictionary.
	filenames = glob.glob('*')
	filenames_dict = {}
	md5_dict = {}
	for filename in filenames:
		if os.path.isdir(filename):
			continue
		else:
			md5 = load_md5(filename)
			filenames_dict[filename] = md5
			md5_dict[md5] = filename

	# Create filenames file
	fo_filenames = open(".damnit/filenames_dict.json" , "w")
	json.dump(filenames_dict, fo_filenames)
	fo_filenames.close()
	print(filenames_dict)

	# Create md5 file
	fo_md5 = open(".damnit/md5_dict.json" , "w")
	json.dump(md5_dict, fo_md5)
	fo_md5.close()
	print(md5_dict)
	
	return all_file_name_dict


if __name__ == '__main__':
	all_file_name_dict()




