'''
This program may not work for you because I am working on it right now!
'''
from geometry import *
from browser import *

space = CartesianSpace()

# TODO: This doesn't quite work when the axis is nearly anti-parrallel to e3.
# The correct solution is not to supply an axis. but instead to supply an attitude.
# The type of this parameter will be a Quaternion or Euclidean3 rotor (as appropriate).
shape = ArrowBuilder().color(0xFFFF00).scale(3).build()
space.add(shape)

workbench = Workbench(space.renderer, space.camera)

timeOut = 6000

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeOut = 0

def setUp():
    # TODO: Need to fix the entire graphics API now we are moving from Vector3, Quaternion to Euclidean3.
#    space.camera.position.set(1.5, 1.5, 1.5)
#    space.camera.lookAt(space.origin)
    workbench.setUp()

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    workbench.tearDown()
    
WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
