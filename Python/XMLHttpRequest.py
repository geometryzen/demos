from http import *

def reqListener():
    print "Aha!"

request = XMLHttpRequest()

request.onload = reqListener

request.open('GET', 'http://localhost:8080/users/geometryzen/repos/demos/blob/master/Python/XMLHttpRequest.py', True)

request.send()


print "Done"
