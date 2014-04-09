# UrlLib.py
import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'gttp://google.com/')

print r


'''
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()

print data
'''