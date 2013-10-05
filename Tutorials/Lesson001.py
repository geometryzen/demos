from browser import WindowAnimationRunner

def tick(t):
    pass

def terminate(t):
    return False

def setUp():
    pass

def tearDown():
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
