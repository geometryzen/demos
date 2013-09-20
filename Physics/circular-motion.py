'''
This example demonstrates circular motion using geometric angles and rotors.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi, exp
from units import *

space = CartesianSpace()

# TODO: This will be simplified by consolidating Euclidean3 and Vector3, Quaternion.
shape = ConeBuilder().color(0xFFFF00).build()#.scale(1).axis(Vector3(1,0,0)).build()
space.add(shape)
print shape.attitude

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)

# The geometric angular velocity measure (quantity with unit-of-measure).
# The angular velocity describes a motion of one revolution every 12 seconds in the x-y plane, counterclockwise.
omega = 2 * pi * i * j / (12 * second)

timeOut = 12 * kilo# * milli * second

workbench = Workbench(space.renderer, space.camera)

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeOut = 0

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(elapsed):
    t = ScalarE3(elapsed) * milli * second
    angle = omega * t / 2
    R = exp(-angle)
    position = (R * (4 * i * meter) * ~R).quantity
    # TODO: When Euclidean3 has been consolidated with Vector3 and Quaternion, this will be much easier.
    shape.position.set(position.x, position.y, position.z)
    # To convert a Euclidean3 rotor to a Quaternion, use the 'dual' parts with a sign change.
    # The quaternion property of the mesh is what we would call the attitude - a spinor.
    shape.attitude = R.quantity
#    shape.quaternion.set(-R.quantity.yz, -R.quantity.zx, -R.quantity.xy, R.quantity.w)
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
