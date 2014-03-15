from three import *
from browser import *
from workbench import *
from math import pi

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100.0

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

material = MeshNormalMaterial()

mesh = Mesh(SphereGeometry(50.0, 32, 24), material)

scene.add(mesh)

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)

def terminate(t):
    return t > 6

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
