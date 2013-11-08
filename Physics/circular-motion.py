'''
This example demonstrates circular motion using geometric angles and rotors.
'''
from geometry import *
from e3ga import *
from browser import *
from workbench import *
from math import pi, exp

timeOut = 12.0

space = CartesianSpace()

shape = ConeBuilder().color(0xFFFF00).build()
space.add(shape)

i = VectorE3(1.0, 0.0, 0.0)
j = VectorE3(0.0, 1.0, 0.0)
k = VectorE3(0.0, 0.0, 1.0)

# The geometric angular velocity quantity.
# The angular velocity describes a motion of one revolution every timeOut seconds in the x-y plane, counterclockwise.
omega = 2.0 * pi * i * j / timeOut

workbench = Workbench(space.renderer, space.camera)

def onDocumentKeyDown(event):
    global timeOut
    if event.keyCode == 27:
        timeOut = 0

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(t):
    R = exp(-omega * t / 2.0)
    shape.position = R * (4 * i) * ~R
    shape.attitude = R
    space.render()
    
def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
