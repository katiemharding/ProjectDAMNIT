#!/usr/bin/env python3

import sys
from damnit_IO import read_json
import os
from md5_module import load_md5
import json

# Create a script to re create a file 

# Define imported file name
new_file = sys.argv[1]



# Convert new file into md5
md5 = load_md5(new_file)

# Open and read md5Graph_NewToOld.json file
original_md5Graph = read_json(".damnit/md5Graph_NewToOld.json")



if md5 in original_md5Graph:
	print(original_md5Graph[md5])









