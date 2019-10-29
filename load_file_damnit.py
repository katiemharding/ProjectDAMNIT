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


DirectoryPath = '/projects/damnit/share/'


form = cgi.FieldStorage()  # parse form data

print("Content-type:text/html\n")  # header plus blank line
print('<html><head>')
print('<title>Project Damnit Input Form</title><br>')  # add a title
print('</head>')
print('<body>')
print('<form method=POST enctype="multipart/form-data" action="./load_file_damnit.py">')
print('<h1>Please select a file to upload</h1>')
print('New File <input type=file name=NewFile>')
print('<input type=submit value="Upload File", name=button>')
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
        fn = os.path.basename(fileitem.filename)
         
        open('/projects/damnit/share/.damnit/' + fn, 'wb').write(fileitem.file.read())
    
        message = 'The file "' + fn + '" was uploaded successfully'
        print(fileitem, '<br>')
        status_damnit(str(fileitem))
    else:
        message = 'please select and submit another file'
    
print("did the file load?<br>")
print(message)
print('</body>')
print('</html>')

