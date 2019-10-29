#!/usr/bin/env python3

from damnit_IO import read_json
from damnit_IO import write_json
import sys
import os.path
import json
from md5_module import load_md5
from generateNewPatch import load_patch_dict




# Define imported file name
#new_file = sys.argv[1]

def add_damnit(new_file, damnit_path = '.damnit'):
	# Check if file exists
	if os.path.exists(new_file):
		print ('File is real')
	else:
		print('File is not real')
	# we want to exit if file does not exist

	# Convert new file into md5
	md5 = load_md5(new_file)

	md5Graph = {}

	# Open and read md5Graph_NewToOld.json file
	original_md5Graph = read_json(damnit_path + "/md5Graph_NewToOld.json")

	# Open and read filenames_dict.json file
	filenames_dict = read_json(damnit_path + "/filenames_dict.json")


	# Check if file is in database
	if new_file in filenames_dict and md5 in original_md5Graph:
		print('File is in database')
		sys.exit(0)
	elif new_file in filenames_dict and md5 not in original_md5Graph:
		load_patch_dict(new_file, damnit_path)
		#fo_Graph = open(damnit_path + "/md5Graph_NewToOld.json" ,"w")
		#json.dump(original_md5Graph, fo_Graph)
		print('Updating file')

	if new_file not in filenames_dict and md5 in original_md5Graph:
		print('File exists by a different name:')
		sys.exit(0)
	elif new_file not in filenames_dict and md5 not in original_md5Graph:
		load_patch_dict(new_file, damnit_path)
		#fo_Graph = open(damnit_path + "/md5Graph_NewToOld.json" ,"w")
		#json.dump(original_md5Graph, fo_Graph)
		print('Adding file to database')
		 




	# Check if md5 exists in md5_dict.json file
#	if md5 in original_md5Graph:
#		print('File exists in database')
#		add_filenames_dict = {}
#		add_filenames_dict[new_file] = md5
#		filenames_dict.update(add_filenames_dict)
#		write_filenames_dict = write_json(damnit_path + "/filenames_dict.json", filenames_dict)
#	else:
#		print('Updating file')
#		add_md5_to_md5Graph = {}
#		add_md5_to_md5Graph[md5] = "none"
#		original_md5Graph.update(add_md5_to_md5Graph)
#		write_md5Graph_dict = write_json(damnit_path + "/md5Graph_NewToOld.json", original_md5Graph)

#		if new_file in filenames_dict:
#			print('File is up to date')
#		else:
#			print('New file does not exist in datebase')
#			# add unknown file to filesnames_dict.json file
#			add_filenames_dict = {}
#			add_filenames_dict[new_file] = md5
#			filenames_dict.update(add_filenames_dict)
#			write_filenames_dict = write_json(damnit_path + "/filenames_dict.json", filenames_dict)		

			# Add unkown md5 file to md5Graph_NewToOld.json file
#			add_md5_to_md5Graph = {}
#			add_md5_to_md5Graph[md5] = "none"
#			original_md5Graph.update(add_md5_to_md5Graph)
#			write_md5Graph_dict = write_json(".damnit/md5Graph_NewToOld.json", original_md5Graph)


if __name__ == '__main__':
	
	new_file = sys.argv[1]
	add_damnit(new_file)












