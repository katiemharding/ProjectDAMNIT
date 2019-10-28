#! /usr/bin/env python3

import sys
import subprocess
import glob
from md5_module import load_md5
import json
import shutil

DamnitPath = '.damnit/'

def find_diff(new_file, old_file):
	file_diff = subprocess.run(['diff', new_file, old_file], stdout = subprocess.PIPE)
	file_stdout = file_diff.stdout
	diff_list = file_stdout.split()
	return diff_list 
# the code in the command line: diff --unified=0 new_file, old_file


def load_patch_dict(FileNameDictionary, md5Graph_NewToOld):
	for indivFile in fileList:
		if indivFile in FileNameDictionary:
			newMD5 = load_md5(indivFile) # find the md5 of the new file
			oldMD5 = FileNameDictionary[indivFile] # for ease of reading, rename the file
			if newMD5 == oldMD5: # if the new md5 is the same as the old md5 do nothing.
				print("no change to", indivFile)
			else: # if the file is the same and the file has changed:
			# Process:
			# 1) find the difference between the files (the path
			# 2) the graph dictionary is the new MD5 as key and the old MD5 as value
			# 3) change the file name dictionary to the new value (the new MD5)
			# 4) copy the file to DamnitPath directory the name of this file is the MD5
			# 5) copy the Patch to the DamnitPath directory, the name is the old MD5
			# !!!!!!!!!!! this will overwright the old file, and all the data in it. !!!!!!!!
				difference = find_diff(indivFile, (DamnitPath + oldMD5)) # this is the patch
				md5Graph_NewToOld[newMD5] = oldMD5 # add in the new md5 as a key, the old md5 is the value
				FileNameDictionary[indivFile] = newMD5 # the file name is now linked to the new MD5 (old one lost)
				with open(sys.argv[1], "w") as newFileDict:
					json.dump(FileNameDictionary, newFileDict)
				with open("md5Graph_NewToOld.json", "w") as newPatch:
					json.dump(md5Graph_NewToOld, newPatch) # open the file as write, save new dict


				print(indivFile,difference, "has changed")
		else: # now the file name is not tracked, and it is not in the dictionary
		# Process: 
		# 1) we need to generate the new file MD5, add it to the dictionary
		# 2) save the new filename dictionary
		# 3) add the file to the the graph dictionary.
		# 4) save the graph dictionary
			newFilemd5 = load_md5(indivFile) # for this new file get a new md5
			FileNameDictionary[indivFile] = newFilemd5 # add it to the file name dictionary
			with open(sys.argv[1], "w") as newFileDict:
				json.dump(FileNameDictionary, newFileDict)
			# old version created the graph file.  since it is now created we don't need it anymore
			md5Graph_NewToOld[newFilemd5] = "none" # since there are no changes, the first value will be none
			with open("md5Graph_NewToOld.json", "w") as newPatch:
				json.dump(md5Graph_NewToOld, newPatch) # open the file as write, save new dict
			print("new file", indivFile) 
	print(FileNameDictionary)

if __name__ == '__main__':
	fnd = json.load(open(sys.argv[1], "r")) # open the file name dictionary
	fileList = glob.glob('*.fasta') # search for new files
	load_patch_dict(fnd) # run the load patch function
