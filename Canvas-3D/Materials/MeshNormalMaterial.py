from three import *
from browser import *
from workbench import *
from math import pi

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100.0

renderer = WebGLRenderer()
renderer.autoClear   = True
renderer.gammaInput  = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

material = MeshNormalMaterial()

mesh = Mesh(SphereGeometry(50.0, 32, 24), material)

scene.add(mesh)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    renderer.render(scene, camera)

def terminate(t):
    return t > 6

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
