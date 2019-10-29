#! /usr/bin/env python3

import sys
import subprocess
import glob
from md5_module import load_md5
import json
import shutil
from damnit_IO import write_json

md5Graph = {}
md5Graph_NewToOld = write_json(".damnit/md5Graph_NewToOld.json", md5Graph)


DamnitPath = '.damnit/'
md5Graph_NewToOld_location = DamnitPath + 'md5Graph_NewToOld.json'
FileNameDictionary_location = DamnitPath + 'filenames_dict.json'


def find_diff(new_file, old_file):
	oldMD5 = load_md5(old_file)
	string = "diff {} {} > {}.patch"
	command = string.format(new_file,old_file,oldMD5)
	subprocess.run(command, shell = True)
# the code in the command line: diff new_file old_file >filename
# apparently we don't need --unified=0

def load_patch_dict(FileNameDictionary, md5Graph_NewToOld):
	for indivFile in fileList:
		newMD5 = load_md5(indivFile) # find the md5 of the new file
		if indivFile in FileNameDictionary:
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
				shutil.copyfile(indivFile, (DamnitPath+newMD5))
				shutil.copyfile((oldMD5+".patch"), (DamnitPath + oldMD5))
				md5Graph_NewToOld[newMD5] = oldMD5 # add in the new md5 as a key, the old md5 is the value
				FileNameDictionary[indivFile] = newMD5 # the file name is now linked to the new MD5 (old one lost)
				with open(FileNameDictionary_location, "w") as newFileDict:
					json.dump(FileNameDictionary, newFileDict)
				with open(md5Graph_NewToOld_location, "w") as newPatch:
					json.dump(md5Graph_NewToOld, newPatch) # open the file as write, save new dict
				
				print(indivFile, "has changed")
		else: # now the file name is not tracked, and it is not in the dictionary
		# Process: 
		# 1) we need to generate the new file MD5, add it to the dictionary
		# 2) save the new filename dictionary
		# 3) add the file to the the graph dictionary.
		# 4) save the graph dictionary
			shutil.copyfile(indivFile, (DamnitPath+newMD5))
			FileNameDictionary[indivFile] = newMD5 # add it to the file name dictionary
			with open(FileNameDictionary_location, "w") as newFileDict:
				json.dump(FileNameDictionary, newFileDict)
			# old version created the graph file.  since it is now created we don't need it anymore
			md5Graph_NewToOld[newMD5] = "none" # since there are no changes, the first value will be none
			with open(md5Graph_NewToOld_location, "w") as newPatch:
				json.dump(md5Graph_NewToOld, newPatch) # open the file as write, save new dict
			print("new file", indivFile) 
	print(FileNameDictionary)

if __name__ == '__main__':
	fnd = json.load(open(FileNameDictionary_location, "r")) # open the file name dictionary
	md5dict = json.load(open(md5Graph_NewToOld_location, "r"))
	fileList = glob.glob('*.fasta') # search for new files
	load_patch_dict(fnd, md5dict) # run the load patch function
