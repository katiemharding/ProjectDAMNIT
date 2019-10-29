#!/usr/bin/env python3
import cgi
import cgitb
import os

DirectoryPath = '/projects/damnit/share/'

cgitb.enable()

form = cgi.FieldStorage()  # parse form data

print("Content-type:text/html\n")  # header plus blank line
print('<html><head>')
print('<title>Project Damnit Input Form</title><br>')  # add a title
print('</head>')
print('<body>')
print('<form method=POST enctype="multipart/form-data" action="./test_cgi.py">')
print('<h1>Please select a file to upload</h1>')
print('New File <input type=file name=NewFile>')
print('<input type=submit value="Upload File", name=button>')
print('</form>')

fileitem = form['NewFile']

# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('/projects/damnit/share/.damnit/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'please select and submit a file'
    
print("did the file load?<br>")
print(message)
print('</body>')
print('</html>')

