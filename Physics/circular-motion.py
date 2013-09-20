'''
This example demonstrates circular motion using geometric angles and rotors.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi, exp

space = CartesianSpace()

# TODO: This will be simplified by consolidating Euclidean3 and Vector3, Quaternion.
shape = ConeBuilder().color(0xFFFF00).build()#.scale(1).axis(Vector3(1,0,0)).build()
space.add(shape)

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)

# The geometric angular velocity measure (quantity with unit-of-measure).
# The angular velocity describes a motion of one revolution every 12 seconds in the x-y plane, counterclockwise.
omega = 2 * pi * i * j / 12

timeOut = 12 * kilo

workbench = Workbench(space.renderer, space.camera)

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeOut = 0

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(elapsed):
    t = ScalarE3(elapsed) * milli
    R = exp(-omega * t / 2)
    shape.position = (R * (4 * i) * ~R)
    shape.attitude = R
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
