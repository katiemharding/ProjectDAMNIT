# ProjectDAMNIT
## DAta MaNagement Interface Tool (DAMNIT)

The volume of sequencing data being produced continues to out-pace the ability to store and efficiently manage it. I propose a software development project to build a command-line application for managing and archiving data files with a Git-like interface. The software is envisioned to 1) traverse directories on a file system and archive only new or modified files, providing a non-redundant data store; 2) detect files with identical contents (but not necessarily identical names) to already-archived files via SHA checksums; 3) perform file comparison and only store differences (changes) in file contents using time-stamped tarballs; 4) store user-defined file/project metadata; 5) implement an interface to search for and list previously-archived files; and 6) retrieving all root files and apply changes while unarchiving.

Programming concepts required by the project:

Use of common Python data structures, especially dictionary insertion and look-up

Using modules (including os, sys, pickle, subprocess, hashlib)

Interfacing with the operating system using built-in Python functions and the subprocess module

Implementing depth-first and breadth-first recursive algorithms
