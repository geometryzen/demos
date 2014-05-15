'''
Under Construction. Nov 4, 2013 (axis)
'''
from three import *
from geometry import *
from workbench import *
from browser import *

space = CartesianSpace()
timeOut = 3

e2 = VectorE3(0,1,0)

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def setUp():
    workbench.setUp()

    material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2})
    mesh = CylinderBuilder().axis(e2).radius(1).height(4).segments(24).material(material).build()

    space.add(mesh)

def tick(t):
    space.render()
    
def terminate(t):
    return t > timeOut

def tearDown(e):
    workbench.tearDown()
    print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()