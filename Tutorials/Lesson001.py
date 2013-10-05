from browser import WindowAnimationRunner

def tick(t):
    print "The time is now " + str(t)

def terminate(t):
    print "Are we done yet?"
    return t > 1

def setUp():
    pass

def tearDown():
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
