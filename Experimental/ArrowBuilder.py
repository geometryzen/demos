from geometry import *
from browser import *
from workbench import *
from math import exp, pi

space = CartesianSpace()

e3 = VectorE3(0,0,1)

rotor = exp(-BivectorE3(0.0, 1.0, 0.0)*pi/4.0)
shape = ArrowBuilder().scale(2).wireframe(False).color(0x0000FF).axis(e3).segments(12).build()
space.add(shape)

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def setUp():
    space.camera.position = VectorE3(1.5, 1.5, 1.5)
    space.camera.lookAt(space.origin)
    workbench.setUp()

def tick(t):
    space.render()
    
def terminate(t):
    return t > 5

def tearDown(e):
    workbench.tearDown()
    
WindowAnimationRunner(tick, terminate, setUp, tearDown).start()