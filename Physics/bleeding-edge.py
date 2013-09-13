'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi, sin, cos
from units import *

space = CartesianSpace()

cone = ConeBuilder().volume(1).build().translateX(-2.5).translateY(+2.5)
space.add(cone)

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
I = i * j
# We seek to describe the angular velocity geometrically and then apply it to rotate the object.
# This will probably require looking at the generator of the rotation and then using the exponential
# function to get the finite rotation.
omega = I * (2 * pi / (16 * second))

timeout = 600000

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeout = 0

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
    t = elapsed * second / 1000
    # TODO: Measure needs to support cosine and sine.
    c = cos(omega * t)
    s = sin(omega * t)
    Is = I * s
    # This looks like exp(I omega)
    r = (c - Is) * i * (c + Is)
    cone.position.set(r.x, r.y, r.z)
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
