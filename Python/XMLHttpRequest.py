from browser import window

url = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'

request = window.XMLHttpRequest()
request.open("GET", url, False)
request.send()

print request.responseText