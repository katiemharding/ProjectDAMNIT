# ProjectDAMNIT
## DAta MaNagement Interface Tool (DAMNIT)

The volume of sequencing data being produced continues to out-pace the ability to store and efficiently manage it. 

What do you do with files that are too big to fit on GitHub?

We have been developing a file storage system that will use AWS to store large files, and a series of python scrips to track changes in and store these files.  

#### During this project we:
1. Developed an Initilization program to start the data file storage system.  This includes building the directory structure, and initializing the dictionaries for tracking files.
2. Wrote a program to create a unique variable based on the file contents (checksum or md5)
3. New additions to the data base are added and tracked with a python script that traverses a dictionary on a file system and archives only new or modified files, providing a non-redundant data store.  
4. New additions are compared with existing files, and the differences to previous versions are compared and stored.  This means that each entry is not stored in the data base saving memory and time.  
5. Developed a website that can be used to add in new files and track existing files in the database.

#### Future upgrades will include:
1. Detect files with identical contents (but not necessarily identical names) to already-archived files via SHA checksums. 
2. store user-defined file/project metadata
3. Retrieve root files (previous versions of stored files) and revert to older versions of stored files

#### Programming concepts required by the project:
- Use of common Python data structures, especially dictionary insertion and look-up
- Using modules (including os, sys, glob, subprocess)
- Interfacing with the operating system using built-in Python functions and the subprocess module
- Implementing depth-first and breadth-first recursive algorithms

### Some cool things we have learned:

#### How to initialize a directory:
what did you learn while working on this part?

#### What are check sums, what do they do.  
 show load_md5 code

#### Steps in adding new files and comparing them
adding some code to test

~~~~~~
createDict = {}
print(createDict)


createDict['file_name1'] = 'askdjfhsdflakjsdhfalkdjf'
createDict['file_name2'] = 'aksdjfhadslkjdadjkh'

print(createDict)
for key in createDict:
 print(key, createDict[key])

~~~~~~


#### building a website on aws

- Python scripts can create html websites using print statements (demo code)
- how to upload files to aws using git
- how to upload files to aws using the command line


### and a demo link

