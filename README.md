# ProjectDAMNIT
## DAta MaNagement Interface Tool (DAMNIT)

The volume of sequencing data being produced continues to out-pace the ability to store and efficiently manage it. 

What do you do with files that are too big to fit on GitHub?

We have been developing a file storage system that will use AWS to store large files, and a series of python scrips to track changes in and store these files.  

During this project we:
1. Developed an Initilization program to start the data file storage system.  This includes building the directory structure, and initializing the dictionaries for tracking files.
2. Wrote a program to create a unique variable based on the file contents (checksum or md5)
3. New additions to the data base are added and tracked with a python script that checks if the file is already present, adds new files, and determines if the file is already present.  This file also determines the difference between the new file and any files already existing in the data base.
4. Developed a website that can be used to add in new files and track existing files in the database.

The volume of sequencing data being produced continues to out-pace the ability to store and efficiently manage it. I propose a software development project to build a command-line application for managing and archiving data files with a Git-like interface. The software is envisioned to 1) traverse directories on a file system and archive only new or modified files, providing a non-redundant data store; 2) detect files with identical contents (but not necessarily identical names) to already-archived files via SHA checksums; 3) perform file comparison and only store differences (changes) in file contents using time-stamped tarballs; 4) store user-defined file/project metadata; 5) implement an interface to search for and list previously-archived files; and 6) retrieving all root files and apply changes while unarchiving.

Programming concepts required by the project:

Use of common Python data structures, especially dictionary insertion and look-up

Using modules (including os, sys, pickle, subprocess, hashlib)

Interfacing with the operating system using built-in Python functions and the subprocess module

Implementing depth-first and breadth-first recursive algorithms
