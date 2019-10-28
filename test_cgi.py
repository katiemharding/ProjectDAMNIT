#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()  # parse form data

print ("Content-type:text/html\n")  # header plus blank line
print('<html><head>')
print ('<title>Project Damnit Input Form</title>')  # add a title
print ('</head>')
print ('<body>')
print('<form method=POST action="./test_cgi.py">')
print('<h1>Please select a file to upload'
print('New File <input type=file name=NewFile>')
print('<input type=submit value="Upload File", name=button>')
print('</form>')
if 'NewFile' in form:
    print('Hello<br>')
    if form['NewFile'].file:
        for line in form['NewFile'].file:
            print(line)
print('</body>')
print('</html>')

