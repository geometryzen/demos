from http import *

def reqListener():
    print "Aha!"

request = XMLHttpRequest()
print "request created"
request.onload = reqListener
print "handler connected"
request.open('GET', 'http://localhost:8080/users/geometryzen/repos/demos/blob/master/Python/XMLHttpRequest.py', True)
print "connection open"
request.send()
print "request sent"

print "Done"
