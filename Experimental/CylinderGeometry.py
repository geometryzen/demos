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
    global mesh

    document.removeElementsByTagName('canvas')

    container = document.getElementById("canvas-container")
    container.appendChild(space.renderer.domElement)

    material = MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":2})
    mesh = CylinderBuilder().radius(1).height(4).material(material).build()

    space.add(mesh)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > progressEnd

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeElementsByTagName('canvas')

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()