from three import *
from browser import *
from workbench import *

scene = Scene()
renderer = WebGLRenderer()


workbench = Workbench(renderer, camera)

def tick(t):
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 4

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
