# UrlLib.py
from http import *

request = XMLHttpRequest()

request.open('GET', 'gttp://google.com/')

print "Done"


'''
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()

print data
'''