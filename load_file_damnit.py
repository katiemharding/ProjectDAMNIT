#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import os
import sys

sys.path.insert(0, '/projects/damnit/share/ProjectDAMNIT')
from damnit_IO import read_json
from damnit_IO import write_json
from md5_module import load_md5

from init import make_damnit
from init import all_file_name_dict
from add_md5 import add_damnit
from compare import status_damnit
from generateNewPatch import find_diff
from generateNewPatch import load_patch_dict


DirectoryPath = '/projects/damnit/share/.damnit'


form = cgi.FieldStorage()  # parse form data

print("Content-type:text/html\n")  # header plus blank line
print('<html><head>')
print('<title>Project Damnit Input Form</title><br>')  # add a title
print('</head>')
print('<body>')
print('<form method=POST enctype="multipart/form-data" action="./load_file_damnit.py">')
print('<h1>Please select a file to upload</h1>')
print('New File <input type=file name=NewFile><br>')
#print('File Name Dictionary <input type=file name=NewFileDict><br>')
#print('md5 Dictionary <input type=file name=NewMd5Dict><br>')
print('When ready to test file: <input type=submit value="Test File", name=button>')
print('</form>')
message = 'please select and submit a file'
if 'NewFile' in form:
    print('Thank you for loading a file<br>')
#    if form['NewFile'].value:
#        print("did the file load?")
#        print(form['NewFile'].value)
#        print("file loaded")

    fileitem = form['NewFile']

# Test if the file was uploaded
    if fileitem.filename:
    # strip leading path from file name
    # to avoid directory traversal attacks
        fn = '/'.join([DirectoryPath, os.path.basename(fileitem.filename)])
         
        open(fn, 'wb').write(fileitem.file.read())
        cks = load_md5(fn)
        message = 'The file "' + os.path.basename(fileitem.filename) + '" was uploaded successfully ({})'.format(cks)
        print(message)
        print('<br>')
        status_damnit(fn, DirectoryPath) 
        #print('<br>Upload Now <input type=file name=upload><br>')
        #print('When ready upload file: <input type=submit value="Upload File", name=uploadbutton>')
        #if uploadbutton in form:
        #load_patch_dict(fn, DirectoryPath)
        print('<br>')
         
    else:
        message = 'please select and submit another file'
        print(message)
print('</body>')
print('</html>')

