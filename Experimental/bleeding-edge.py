from three import *
from geometry import *
from browser import *
from math import pi

space = CartesianSpace()
timeOut = 3000

e1 = ArrowBuilder().color(0xFF0000).build()
e1.quaternion.setAxisAngle(Vector3(0,1,0), pi/2)
e3 = ArrowBuilder().color(0x0000FF).build()

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

    space.add(e1)
    space.add(e3)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()