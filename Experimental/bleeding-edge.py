from three import *
from geometry import *
from browser import *

space = CartesianSpace()
timeOut = 3000

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

    mesh = ArrowBuilder().color(0x0000FF).build()

    space.add(mesh)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()