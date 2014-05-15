from three import *
from geometry import *
from browser import *
from workbench import *
from math import pi, exp

space = CartesianSpace()

i = VectorE3(1.0, 0.0, 0.0, False)
j = VectorE3(0.0, 1.0, 0.0, False)
k = VectorE3(0.0, 0.0, 1.0, False)

e1 = ArrowBuilder().color(0xFF0000).axis(i).build()#.attitude(exp(-BivectorE3( 0,  0, 1)*pi/4)).build()
e2 = ArrowBuilder().color(0x00FF00).axis(j).build()#.attitude(exp(-BivectorE3( 0, -1, 0)*pi/4)).build()
e3 = ArrowBuilder().color(0x0000FF).axis(k).build()#.attitude(exp(-BivectorE3( 1,  0, 0)*pi/4)).build()

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
    return t > 10

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()
