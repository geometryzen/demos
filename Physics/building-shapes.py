'''
This example illustrates the builder pattern for creating meshes with a specific geometry.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi

space = CartesianSpace()

space.add(CylinderBuilder().color(0x00FF00).build().translateX(-2.5).translateY(-2.5))
space.add(CubeBuilder().color(0x0000FF).build().translateX(2.5).translateY(2.5))
space.add(SphereBuilder().color(0xFF0000).build().translateX(+2.5).translateY(-2.5))
space.add(ConeBuilder().color(0xFFFF00).build().translateX(-2.5).translateY(+2.5))

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
    print "Press Esc to exit"
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
