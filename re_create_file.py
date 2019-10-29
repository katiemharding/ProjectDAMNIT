#!/usr/bin/env python3

import sys
from damnit_IO import write_json




# Create a script to re create a file 

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


print(original_md5Graph)












