'''
This lesson demonstrates adding a simple object to a scene.
'''
from browser import WindowAnimationRunner
from geometry import CartesianSpace, SphereBuilder
from workbench import Workbench

space = CartesianSpace()

# The object is created using the builder pattern.
sphere = SphereBuilder().color(0x0000FF).build()
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
