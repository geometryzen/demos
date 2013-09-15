'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi, exp
from units import *

space = CartesianSpace()

shape = SphereBuilder().color(0xFFFF00).radius(0.1).build().translateX(-2.5).translateY(+2.5)
space.add(shape)

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)
B = i * j

# The geometric angular velocity measure (quantity with unit-of-measure).
omega = 2 * pi * B / (12 * second)

timeout = 600000

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeout = 0

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
    t = ScalarE3(elapsed / 1000) * second
    angle = omega * t / 2
    R = exp(angle * -1)
    r = R * (4 * i * meter) * (~R)
    position = r.quantity
    shape.position.set(position.x, position.y, position.z)
    space.render()
    
def terminate(elapsed):
    return elapsed > timeout

def setUp():
    document.removeElementsByTagName("canvas")
    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    document.addEventListener("keydown", onDocumentKeyDown, False)
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
