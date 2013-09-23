'''
This program may not work for you because I am working on it right now!
The main change is to unify the quantities used by the graphics API.
Instead of Vector3 and Quaternion we use Euclidean3 (and constructors ScalarE3, VectorE3, BivectorE3, PseudoscalarE3).
'''
from geometry import *
from browser import *
from workbench import *
from math import exp, pi

space = CartesianSpace()

# Specify an attitude as the rotor that rotates e2(j) onto e3(k)
rotor = exp(-BivectorE3(0,1,0)*pi/4)
print rotor
shape = ArrowBuilder().wireframe(False).color(0x0000FF).attitude(rotor).build()
space.add(shape)

workbench = Workbench(space.renderer, space.camera)

def setUp():
    space.camera.position = VectorE3(1.5, 1.5, 1.5)
    space.camera.lookAt(space.origin)
    workbench.setUp()

def tick(t):
    space.render()
    
def terminate(t):
    return t > 5

def tearDown():
    workbench.tearDown()
    
WindowAnimationRunner(tick, terminate, setUp, tearDown).start()