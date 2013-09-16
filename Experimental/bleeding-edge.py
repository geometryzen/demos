from three import *
from geometry import *
from browser import *
from math import pi

space = CartesianSpace()
timeOut = 6000

e1 = ArrowBuilder().color(0xFF0000).build()
e1.quaternion.setFromAxisAngle(Vector3(0,1,0), +pi/2)
e2 = ArrowBuilder().color(0x00FF00).build()
e2.quaternion.setFromAxisAngle(Vector3(1,0,0), -pi/2)
e3 = ArrowBuilder().color(0x0000FF).build()

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

    space.add(e1)
    space.add(e2)
    space.add(e3)
    
    space.camera.position.set(2,2,2)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()