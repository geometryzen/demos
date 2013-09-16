from three import *
from geometry import *
from browser import *

space = CartesianSpace()
timeOut = 3000

e3 = ArrowBuilder().length(1).color(0x0000FF).build()

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

    space.add(e3)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()