from browser import window

url = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
clazz = window.XMLHttpRequest

print clazz

request.open("GET", url, False)
request.send()

print request.responseText