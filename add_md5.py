#!/usr/bin/env python3

from damnit_IO import read_json
from damnit_IO import write_json
import sys
import os.path
import json
from md5_module import load_md5


# Define imported file name
new_file = sys.argv[1]

# Check if file exists
if os.path.exists(new_file):
	print ('File is real')
else:
	print('File is not real')
# we want to exit if file does not exist

# Convert new file into md5
md5 = load_md5(new_file)


# Open and read md5Graph_NewToOld.json file
original_md5Graph = read_json(".damnit/md5Graph_NewToOld.json")

# Open and read filenames_dict.json file
filenames_dict = read_json(".damnit/filenames_dict.json")


# Check if md5 exists in md5_dict.json file
if md5 in original_md5Graph:
	print('File exists in md5Graph_NewToOld.json')
	add_filenames_dict = {}
	add_filenames_dict[new_file] = md5
	filenames_dict.update(add_filenames_dict)
	write_filenames_dict = write_json(".damnit/filenames_dict.json", filenames_dict)
else:
	print('File does not exist in md5Graph_NewToOld.json')
	add_md5_to_md5Graph = {}
	add_md5_to_md5Graph[md5] = "none"
	original_md5Graph.update(add_md5_to_md5Graph)
	write_md5Graph_dict = write_json(".damnit/md5Graph_NewToOld.json", original_md5Graph)

	if new_file in filenames_dict:
		print('File exists in filesnames_dict.json')
	else:
		print('File does not exist in filesnames_dict.json')
		# add unknown file to filesnames_dict.json file
		add_filenames_dict = {}
		add_filenames_dict[new_file] = md5
		filenames_dict.update(add_filenames_dict)
		write_filenames_dict = write_json(".damnit/filenames_dict.json", filenames_dict)		

		# Add unkown md5 file to md5Graph_NewToOld.json file
		add_md5_to_md5Graph = {}
		add_md5_to_md5Graph[md5] = "none"
		original_md5Graph.update(add_md5_to_md5Graph)
		write_md5Graph_dict = write_json(".damnit/md5Graph_NewToOld.json", original_md5Graph)




#print(original_md5['8ac6f00a5de4ef1b08da1bdf4668440f'])




# if md5 is not in 
# if md5 is same for 2 files then add new file to file_dict
# if md5 in not 














