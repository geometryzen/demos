from http import *

def reqListener():
    print "Aha!"

request = XMLHttpRequest()
print "request created"
request.onload = reqListener
print "handler connected"
request.open('GET', 'https://github.com/david-geo-holmes', True)
print "connection open"
request.send()
print "request sent"

print "Done"
