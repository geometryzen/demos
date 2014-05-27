from three import *
from geometry import *
from browser import *
from workbench import *
from math import pi, exp

space = CartesianSpace()
timeOut = 10

# Arrows are assumed to be aligned with the y-axis, so we must adjust their attitudes.
e1 = ArrowBuilder().color(0xFF0000).attitude(exp(-BivectorE3(-1.0, 0.0, 0.0)*pi/4.0)).build()
e2 = ArrowBuilder().color(0x00FF00).attitude(exp(-BivectorE3( 0.0, 0.0, 0.0)*pi/4.0)).build()
e3 = ArrowBuilder().color(0x0000FF).attitude(exp(-BivectorE3( 0.0, 1.0, 0.0)*pi/4.0)).build()

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def setUp():
    workbench.setUp()

    space.add(e1)
    space.add(e2)
    space.add(e3)
    
    space.camera.position.set(2.0, 2.0, 2.0)
    space.camera.lookAt(VectorE3(0.0, 0.0, 0.0))

def tick(t):
    space.render()
    
def terminate(t):
    return t > timeOut

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
