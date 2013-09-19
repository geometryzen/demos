'''
This program may not work for you because I am working on it right now!
The main change is to unify the quantities used by the graphics API.
Instead of Vector3 and Quaternion we use Euclidean3 (and constructors ScalarE3, VectorE3, BivectorE3, PseudoscalarE3).
'''
from geometry import *
from browser import *

space = CartesianSpace()

# TODO: This doesn't quite work when the axis is nearly anti-parrallel to e3.
# The correct solution is not to supply an axis. but instead to supply an attitude.
# The type of this parameter will be a Quaternion or Euclidean3 rotor (as appropriate).
rotor = exp(-BivectorE3(0,0,1)*pi/4)
print rotor
builder = ArrowBuilder().color(0xFFFF00).axis(Vector3(1,0,0).normalize())
shape = builder.build()
space.add(shape)

workbench = Workbench(space.renderer, space.camera)

def setUp():
    space.camera.position = VectorE3(1.5, 1.5, 1.5)
    space.camera.lookAt(space.origin)
    workbench.setUp()

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 5000

def tearDown():
    workbench.tearDown()
    
WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()