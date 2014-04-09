# UrlLib.py
import urllib3

pool = urllib3.PoolManager()

r = pool.request('GET', 'gttp://google.com/')

print r


'''
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()

print data
'''