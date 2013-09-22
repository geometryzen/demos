# The purpose of this experiment is to see if the details of a general example can be reproduced using convenience functions.
from three import *
from geometry import CartesianSpace, CylinderBuilder
from workbench import *
from browser import document, window, Workbench3D, WindowAnimationRunner

space = CartesianSpace()
progressEnd = 6

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def setUp():
    workbench.setUp()

    material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2})
    mesh = CylinderBuilder().radius(1).height(4).material(material).build()

    space.add(mesh)

def tick(t):
    space.render()
    
def terminate(t):
    return t > progressEnd

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()