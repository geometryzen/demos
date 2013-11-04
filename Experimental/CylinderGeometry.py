from three import *
from geometry import *
from workbench import *
from browser import *

space = CartesianSpace()
timeOut = 3

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

def setUp():
    workbench.setUp()

    material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2})
    mesh = CylinderBuilder().axis(e1).radius(1).height(4).segments(3).material(material).build()

    space.add(mesh)

def tick(t):
    space.render()
    
def terminate(t):
    return t > timeOut

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()