#! /usr/bin/env python3

import subprocess
import glob
from md5_module import load_md5

fileList = glob.glob('*.fasta')



fileDict = dict()

def load_patch_dict(FileNameDictionary):
	for indivFile in fileList:
		if indivFile in FileNameDictionary:
			newCheckSum = load_md5(indivFile)
			if newCheckSum == FileNameDictionary[indivFile]:
				print("no change to", indivFile)
			else:
				print(indivFile, "has changed")
		else:
			print("new file", indivFile)

if __name__ == '__main__'
	with open(sys.argv[1], "r") as FND:
		load_patch_dict(FND)
