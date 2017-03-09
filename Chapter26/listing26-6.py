#!/usr/bin/python

print('Content-type: text/html\n')

import cgitb; cgitb.enable()

import psycopg2
conn = psycopg2.connect('user=foo password=bar dbname=baz')
curs = conn.cursor()

import cgi, sys
form = cgi.FieldStorage()
id = form.getvalue('id')

print("""
<html>
  <head>
    <title>View Message</title>
  </head>
  <body>
    <h1>View Message</h1>
    """)

try: id = int(id)
except:
     print('Invalid message ID')
     sys.exit()

curs.execute('SELECT * FROM messages WHERE id = %s', (format(id),))
rows = curs.dictfetchall()

if not rows:
     print('Unknown message ID')
     sys.exit()

row = rows[0]

print("""
     <p><b>Subject:</b> {subject}<br />
     <b>Sender:</b> {sender}<br />
     <pre>{text}</pre>
     </p>
     <hr />
     <a href='main.cgi'>Back to the main page</a>
     | <a href="edit.cgi?reply_to={id}">Reply</a>
  </body>
</html>
""".format(row))