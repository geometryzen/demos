from browser import WindowAnimationRunner
from geometry import CartesianSpace, SphereBuilder
from workbench import Workbench

space = CartesianSpace()

sphere = SphereBuilder().build()
space.add(sphere)

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    space.render()

def terminate(t):
    done = t > 4
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()