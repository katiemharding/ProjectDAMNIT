#! /usr/bin/env python3

import sys
import json


DamnitPath = '.damnit/'
md5Graph_NewToOld_location = DamnitPath + 'md5Graph_NewToOld.json'
FileNameDictionary_location = DamnitPath + 'quickDict.json'

File_Name = ''
try:
	File_Name = sys.argv[1]
	print("User provided file: ", File_Name)
	if not File_Name.endswith('.fasta'):
		raise ValueError("not a .fasta file")
	FileNameDictionary = json.load(open(FileNameDictionary_location, "r")) # open the file name dictionary
	if File_Name in FileNameDictionary:
		print("file found:", File_Name)
		with open(DamnitPath, FileNameDictionary[File_name]) as fileobject:
			print(fileobject)

except IndexError:
	print("Please provide file Name")
except IOError as ex:
	print(File_Name, ": Doesn't exist, ", ex.strerror)
