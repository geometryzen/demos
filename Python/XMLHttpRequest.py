from http import *

def reqListener():
    print "Aha!"

request = XMLHttpRequest()
print "request created"
request.onload = reqListener
print "handler connected"
request.open('GET', 'localhost:8080/', True)
print "connection open"
request.send()
print "request sent"

print "Done"


'''
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()

print data
'''