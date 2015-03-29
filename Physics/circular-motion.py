'''
This example demonstrates circular motion using geometric angles and rotors.
'''
from geometry import *
from e3ga import *
from browser import *
from workbench import *
from math import pi, exp

space = CartesianSpace()

shape = ConeBuilder().color(0xFFFF00).build()
space.add(shape)

i = VectorE3(1.0, 0.0, 0.0)
j = VectorE3(0.0, 1.0, 0.0)
k = VectorE3(0.0, 0.0, 1.0)

# The geometric angular velocity quantity.
# The angular velocity describes a motion of one revolution every timeOut seconds in the x-y plane, counterclockwise.
omega = 2.0 * pi * i * j / 1

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

frames = 0.0
elapsed = 0.0
timeout = 10.0

def setUp():
    workbench.setUp()

def tick(t):
    global frames, elapsed
    frames += 1.0
    elapsed = t
    print t
    R = exp(-omega * t / 2.0)
    shape.position = R * i * ~R
    print shape.position
#   shape.attitude = R
    space.render()
    
def terminate(t):
    return t > timeout

def tearDown(e):
    workbench.tearDown()
    print frames / elapsed
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
