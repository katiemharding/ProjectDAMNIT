#! /usr/bin/env python3

import sys
import subprocess
import glob
from md5_module import load_md5
import json

fileList = glob.glob('*.fasta')

def load_patch_dict(FileNameDictionary):
	for indivFile in fileList:
		if indivFile in FileNameDictionary:
			newCheckSum = load_md5(indivFile)
			if newCheckSum == FileNameDictionary[indivFile]:
				print("no change to", indivFile)
			else:
				print(indivFile, "has changed")
		else:
			FileNameDictionary[indivFile] = load_md5(indivFile)
			print("new file", indivFile)
	print(FileNameDictionary)

if __name__ == '__main__':
	fnd = json.load(open(sys.argv[1], "r"))

	with open(sys.argv[2], "w") as newdict:
		newdict = load_patch_dict(fnd)

