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
print('New File <input type=text name=NewFile>')
print('<input type=submit value="Upload File", name=button>')
print('</form>')
if 'NewFile' in form:
    print('Hello')
print('</body>')
print('</html>')

