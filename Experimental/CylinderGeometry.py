from three import *
from geometry import *
from workbench import *
from browser import *

space = CartesianSpace()
timeOut = 6

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def setUp():
    workbench.setUp()

    material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2})
    mesh = CylinderBuilder().radius(1).height(4).material(material).build()

    space.add(mesh)

def tick(t):
    space.render()
    
def terminate(t):
    return t > timeOut

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()