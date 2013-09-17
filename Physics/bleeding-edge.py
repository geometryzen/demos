'''
This program may not work for you because I am working on it right now!
'''
from geometry import *
from browser import *

space = CartesianSpace()

builder = ArrowBuilder().color(0xFFFF00).axis(Vector3(0,-1,0))
shape = builder.build()
space.add(shape)

workbench = Workbench(space.renderer, space.camera)

def setUp():
    space.camera.position.set(1.5, 1.5, 1.5)
    space.camera.lookAt(space.origin)
    workbench.setUp()

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 5000

def tearDown():
    workbench.tearDown()
    
WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
