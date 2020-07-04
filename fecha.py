# Import modules for CGI handling
import cgi, cgitb
# Import datetime modules
from datetime import datetime, timedelta
# Create instance of FieldStorage
index = cgi.FieldStorage()
# Get data from fields and assign date type to a new variable
date_user = index.getvalue('date_user')
date2 = datetime.strptime(date_user,'%Y-%m-%d')
# Get actual date
today = datetime.today()
# Operation dif
dif = today - date2
#Print the results   
print "Content-type:text/html\r\n\r\n"
  print "<html>"
    print "<body>"
      print "<h2>Since %s ,  %s days of difference </h2>" % (date_user, dif.days)
    print "</body>"
  print "</html>"
