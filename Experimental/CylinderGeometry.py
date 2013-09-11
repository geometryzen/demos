# The purpose of this experiment is to see if the details of a general example can be reproduced using convenience functions.
from three import *
from geometry import CartesianSpace, CylinderBuilder
from browser import document, window, WindowAnimationRunner
from math import pi

#scene = Scene()
space = CartesianSpace()
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
renderer = WebGLRenderer({"antialias": True})
mesh = None
progressEnd = 10000
movement = Vector3(0.02, 0.02, 0.02)

def setUp():
    global mesh

    document.removeElementsByTagName('canvas')
    renderer.setClearColor(Color(0x080808), 1.0)

    container = document.getElementById("canvas-container")
    container.appendChild(renderer.domElement)

    camera.position.z = 100

    material = MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3})
    mesh = CylinderBuilder().radius(20).height(100).material(material).build()

    space.add(mesh)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tick(elapsed):
    mesh.rotation += movement
    space.render()
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > progressEnd

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeElementsByTagName('canvas')

def onWindowResize(event):
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()