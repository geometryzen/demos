from http import *

def reqListener():
    # One problem is that we don't have access to this
    print "Aha!"

xhr = XMLHttpRequest()

xhr.open('GET', 'http://localhost:8080/users/geometryzen/repos/demos/blob/master/Python/XMLHttpRequest.py', True)

#xhr.responseType = "text"

xhr.onload = reqListener

xhr.send()


print "Done"
