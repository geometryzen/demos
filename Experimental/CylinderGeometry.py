# The purpose of this experiment is to see if the details of a general example can be reproduced using convenience functions.
from three import *
from geometry import CartesianSpace, CylinderBuilder
from browser import document, window, Workbench, WindowAnimationRunner
from math import pi

#scene = Scene()
space = CartesianSpace()
progressEnd = 6000

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

    material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2})
    mesh = CylinderBuilder().radius(1).height(4).material(material).build()

    space.add(mesh)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > progressEnd

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()