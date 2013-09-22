'''
This example demonstrates coloring shapes and normalizing their volumes to unity.
'''
from geometry import *
from e3ga import *
from browser import *
from workbench import *
from math import pi

space = CartesianSpace()

space.add(CylinderBuilder().color(0x00FF00).volume(1).build().translateX(-2.5).translateY(-2.5))
space.add(CubeBuilder().color(0x0000FF).volume(1).build().translateX(2.5).translateY(2.5))
space.add(SphereBuilder().color(0xFF0000).volume(1).build().translateX(+2.5).translateY(-2.5))
space.add(ConeBuilder().color(0xFFFF00).volume(1).build().translateX(-2.5).translateY(+2.5))

timeOut = 6

workbench = Workbench(space.renderer, space.camera)

def onDocumentKeyDown(event):
    global timeOut
    if event.keyCode == 27:
        timeOut = 0

def tick(t):
    space.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
