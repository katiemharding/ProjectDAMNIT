#!/usr/bin/env python3

import glob
import json




# bring in a json file to read
def read_json(name):
	# This is just a test, need to change to accept any .json
	fo_read_json = json.load(open(name , "r"))
	return fo_read_json






# make and write a json file
def write_json(name, dictionary):
# Define variable objects in function	
	fo_write_json = open(name , "w")
	json.dump(dictionary, fo_write_json)
#	print(fo_write_json)
#	return fo_write_json








#if __name__ == '__main__':
#	read_json() 



