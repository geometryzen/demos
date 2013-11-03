from three import *
from browser import *
from workbench import *

scene = Scene()


workbench = Workbench(space.renderer, space.camera)

def tick(t):
    space.render()
    
def terminate(t):
    return t > 4

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
