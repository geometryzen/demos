'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi

space = CartesianSpace()

space.add(CylinderBuilder().volume(1).build().translateX(-2.5).translateY(-2.5).rotateX(pi/2).translateZ(0.5))
space.add(CubeBuilder().color("blue").build().translateX(2.5).translateY(2.5).translateZ(0.5))
space.add(SphereBuilder().volume(1).color("red").build().translateX(+2.5).translateY(-2.5))

# It's a bit confusing that the local coordinates are rotated!
space.add(ConeBuilder().volume(1).color("yellow").build().rotateX(pi/2).translateY(0.7816).translateX(-2.5).translateZ(-2.5))

timeout = 600000

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeout = 0

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
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
