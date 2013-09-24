from browser import *

def setUp():
    print "setUp"

def tick(t):
    print "tick"

def terminate(t)
    return t > 5

def tearDown():
    print "tearDown"

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
