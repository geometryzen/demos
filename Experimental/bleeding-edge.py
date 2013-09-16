from three import *
from geometry import CartesianSpace, CylinderBuilder
from browser import document, window, Workbench, WindowAnimationRunner

space = CartesianSpace()
progressEnd = 6000

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

    mesh = CylinderBuilder().build()

    space.add(mesh)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > progressEnd

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()