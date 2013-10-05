from browser import WindowAnimationRunner

def tick(t):
    print "The time is now " + str(t)

def terminate(t):
    done = t > 1
    print "Are we done yet? " + str(done)
    return done

def setUp():
    pass

def tearDown():
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
