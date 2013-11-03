from three import *
from browser import *
from workbench import *
from random import random

scene = Scene()
renderer = WebGLRenderer()
renderer.sortObjects = False
camera = PerspectiveCamera(70, 1, 1, 10000)

light = DirectionalLight(0xFFFFFF, 2)
light.position.set(1, 1, 1).normalize()
scene.add(light)

light = DirectionalLight(0xFFFFFF)
light.position.set(-1, -1, -1).normalize()
scene.add(light)

geometry = CubeGeometry(20, 20, 20)

for i in range(0, 10):
    object = Mesh(geometry, MeshLambertMaterial({"color": random() * 0xFFFFFF}))
    scene.add(object)

workbench = Workbench(renderer, camera)

def tick(t):
    camera.lookAt(scene.position)
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 4

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
