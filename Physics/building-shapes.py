'''
This example illustrates the builder pattern for creating meshes with a specific geometry.
The shapes are drawn with their default linear dimensions and colored white.
'''
from geometry import *
from e3ga import *
from browser import *
from workbench import *
from math import pi

space = CartesianSpace()

space.add(CylinderBuilder().build().translateX(-2.5).translateY(-2.5))
space.add(CubeBuilder().build().translateX(2.5).translateY(2.5))
space.add(SphereBuilder().build().translateX(+2.5).translateY(-2.5))
space.add(ConeBuilder().build().translateX(-2.5).translateY(+2.5))
space.add(ArrowBuilder().build())

timeout = 6

workbench = Workbench(space.renderer, space.camera)

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeout = 0

def tick(t):
    space.render()
    
def terminate(t):
    return t > timeout

def setUp():
    print "Press Esc to exit"
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
