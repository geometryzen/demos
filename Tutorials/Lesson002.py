from browser import WindowAnimationRunner
from geometry import CartesianSpace
from workbench import Workbench

space = CartesianSpace()

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    print "The time is now " + str(t)
    space.render()

def terminate(t):
    done = t > 1
    print "Are we done yet? " + str(done)
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()