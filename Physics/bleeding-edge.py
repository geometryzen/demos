'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi, sin, cos, exp
from units import *

space = CartesianSpace()

cone = ConeBuilder().volume(1).build().translateX(-2.5).translateY(+2.5)
space.add(cone)

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)
I = i * k

# The geometric angular velocity.
omega = 2 * pi * I / 10

timeout = 600000

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeout = 0

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
    t = elapsed / 1000
    # TODO: Measure needs to support cosine and sine.
    angle = omega * t / 2
    R = exp(-angle)
    r = R * i * (~R)
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
