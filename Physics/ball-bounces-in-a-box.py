from browser import *
from three import *

scene = Scene()

renderer = WebGLRenderer()

camera = PerspectiveCamera()

def setUp():
    print "setUp"

def tick(t):
    pass

def terminate(t):
    return t > 1

def tearDown():
    print "tearDown"

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
