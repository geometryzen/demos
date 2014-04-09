from http import *

def reqListener():
    print "Aha!"

request = XMLHttpRequest()

request.open('GET', 'http://google.com/')

request.send()

print "Done"


'''
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()

print data
'''