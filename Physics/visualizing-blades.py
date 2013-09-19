'''
This example demonstrates coloring shapes and normalizing their volumes to unity.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi

space = CartesianSpace()

space.add(CylinderBuilder().color(0x00FF00).volume(1).build().translateX(-2.5).translateY(-2.5))
space.add(CubeBuilder().color(0x0000FF).volume(1).build().translateX(2.5).translateY(2.5))
space.add(SphereBuilder().color(0xFF0000).volume(1).build().translateX(+2.5).translateY(-2.5))
space.add(ConeBuilder().color(0xFFFF00).volume(1).build().translateX(-2.5).translateY(+2.5))

timeout = 6000

workbench = Workbench(space.renderer, space.camera)

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeout = 0

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeout

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
