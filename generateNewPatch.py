#! /usr/bin/env python3

import subprocess
import glob

fileList = glob.glob('*.fasta')

fileDict = dict()
for indvFile in fileList:
	if indivFile in fileDict:
		#newCheckSum = getmd5(indivFile)
		if newCheckSum == fileDict[indivFile]
			print("no change to", indivFile)
		else

		print(indivFile, "has changed")
	else:
		#fileDict[indivFile] = getmd5(indivFile)
		print("new file", indivFile)

		
