'''
This lesson demonstrates adding a simple object to a scene.
'''
from browser import WindowAnimationRunner
from geometry import CartesianSpace, SphereBuilder
from workbench import Workbench

scene = CartesianSpace()

# The object is created using the builder pattern.
sphere = SphereBuilder().color(0x0000FF).position(0,0,1).build()
# Once created, the object must be added to the scene in order to be rendered.
scene.add(sphere)

workbench = Workbench(scene.renderer, scene.camera)

def tick(t):
    scene.render()

def terminate(t):
    done = t > 4
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
