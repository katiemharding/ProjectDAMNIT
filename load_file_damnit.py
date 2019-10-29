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
print('<form method=POST enctype="multipart/form-data" action="./load_file_damnit.py">')
print('<h1>Please select a file to upload</h1>')
print('New File <input type=file name=NewFile>')
print('<input type=submit value="Upload File", name=button>')
print('</form>')
message = 'empty message'
if 'NewFile' in form:
    print('Hello<br>')
    if form['NewFile'].value:
        print("did the file load?")
        print(form['NewFile'].value)
        print("file loaded")

#fileitem = form['NewFile']

# Test if the file was uploaded
#if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
 #   fn = os.path.basename(fileitem.filename)
  
  #FileNameDict = 'filenames_dict.json'
   # open('/projects/damnit/share/.damnit/' + FileNameDict, 'r').write(fileitem.file.read())
    
    #message = 'The file "' + FileNameDict + '" was uploaded successfully'

else:
    message = 'please select and submit a file'
    
print("did the file load?<br>")
print(message)
print('<h1>Files already in storage</h1>')
print('</body>')
print('</html>')

