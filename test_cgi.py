#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()  # parse form data
print ("Content-type:text/html\n")  # header plus blank line
print('<html><head>')
print ('<title>Hello Word - First CGI Program</title>')  # add a title
print ('</head>')
print ('<body>')
print('<form method=POST action="cgi-bin/anotherfile.py">')
print('NewFile <input type=text name=NewFile>')
print('</form>')
print('</body>')
print('</html>')

