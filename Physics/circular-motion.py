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

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(t):
    R = exp(-omega * t / 2.0)
    shape.position = R * i * ~R
#   shape.attitude = R
    space.render()
    
def terminate(t):
    print t
    return t > 5

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
