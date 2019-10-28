#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()  # parse form data
print ("Content-type:text/html\n")  # header plus blank line

print ('<title>Hello Word - First CGI Program</title>')  # add a title
print ('</head>')
print ('<body>')
if not 'user' in form:
	print('<h1>Who are you?</h1>')
else:
	print('<h1>Hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))
</body>
</html>

