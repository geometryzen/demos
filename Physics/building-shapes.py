'''
This example illustrates the builder pattern for creating meshes with a specific geometry.
The shapes are drawn with their default linear dimensions and colored white.
'''
from geometry import *
from e3ga import *
from browser import *
from workbench import *

space = CartesianSpace()

space.add(CylinderBuilder().build().translateX(-2.5).translateY(-2.5))
space.add(CubeBuilder().build().translateX(2.5).translateY(2.5))
space.add(SphereBuilder().build().translateX(+2.5).translateY(-2.5))
space.add(ConeBuilder().build().translateX(-2.5).translateY(+2.5))
space.add(ArrowBuilder().build())

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def tick(t):
    space.render()
    
def terminate(t):
    return t > 6

def setUp():
    workbench.setUp()

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
