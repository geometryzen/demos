from three import *
from browser import *
from workbench import *
from random import random
from math import *

radius = 100.0
omega  = 2.0 * pi / 5.0

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
    object.position.x = random() * 800.0 - 400.0
    object.position.y = random() * 800.0 - 400.0
    object.position.z = random() * 800.0 - 400.0
    
    object.rotation.x = random() * 800.0 - 400.0
    object.rotation.y = random() * 800.0 - 400.0
    object.rotation.z = random() * 800.0 - 400.0
    
    scene.add(object)

workbench = Workbench(renderer, camera)

def tick(t):
    theta = omega * t
    camera.position.x = radius * sin(theta)
    camera.position.y = radius * sin(theta)
    camera.position.z = radius * cos(theta)
    camera.lookAt(scene.position)
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 4

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
