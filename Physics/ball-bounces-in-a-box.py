from browser import *

def setUp():
    print "setUp"

def tick(t):
    pass

def terminate(t):
    return t > 1

def tearDown():
    print "tearDown"

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
