'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi

space = CartesianSpace()

a = CylinderBuilder().name("Cylinder").color(0x00FF00).volume(1).build().translateX(-2.5).translateY(-2.5)
print "a.name => " + a.name
space.add(a)

b = CubeBuilder().name("Cube").color(0x0000FF).volume(1).build().translateX(2.5).translateY(2.5)
print "b.name => " + b.name
space.add(b)

c = SphereBuilder().name("Sphere").color(0xFF0000).volume(1).build().translateX(+2.5).translateY(-2.5)
print "c.name => " + c.name
space.add(c)

d = ConeBuilder().name("Cone").color(0xFFFF00).volume(1).build().translateX(-2.5).translateY(+2.5)
print "d.name => " + d.name
space.add(d)

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
