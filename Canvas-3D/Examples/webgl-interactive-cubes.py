from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text("Hit Esc key to exit.", font, "black")
output.x = 100
output.y = 60
space2D.addChild(output)

radius = 100.0
omega  = 2.0 * pi / 20.0
timeOut = 60.0

mouse = VectorE3(0.0, 0.0, 1.0)
INTERSECTED = None
currentHex = None

scene = Scene()
renderer = WebGLRenderer()
renderer.sortObjects = False
camera = PerspectiveCamera(70, 1, 1, 10000)

light = DirectionalLight(0xFFFFFF, 2)
light.position.set(1.0, 1.0, 1.0).normalize()
scene.add(light)

light = DirectionalLight(0xFFFFFF)
light.position.set(-1.0, -1.0, -1.0).normalize()
scene.add(light)

projector = Projector()
raycaster = Raycaster()

geometry = CubeGeometry(20, 20, 20)

for i in range(0, 2000):
    material = MeshLambertMaterial({"color": random() * 0xFFFFFF})
    mesh = Mesh(geometry, material)

    mesh.position.x = random() * 800.0 - 400.0
    mesh.position.y = random() * 800.0 - 400.0
    mesh.position.z = random() * 800.0 - 400.0

    mesh.rotation.x = random() * 2.0 * pi
    mesh.rotation.y = random() * 2.0 * pi
    mesh.rotation.z = random() * 2.0 * pi
    
    mesh.scale.x = random() + 0.5
    mesh.scale.y = random() + 0.5
    mesh.scale.z = random() + 0.5

    scene.add(mesh)
    
workbench = Workbench3D(renderer.domElement, renderer, camera)

def onDocumentMouseMove(event):
    event.preventDefault()
    mouse.x = (float(event.clientX) / float(window.innerWidth)) * 2.0 - 1.0
    mouse.y = - (float(event.clientY) / float(window.innerHeight)) * 2.0 + 1.0

def tick(t):
    global INTERSECTED, currentHex
    theta = omega * t
    
    camera.position.x = radius * sin(theta)
    camera.position.y = radius * sin(theta)
    camera.position.z = radius * cos(theta)
    camera.lookAt(scene.position)
    
    vector = mouse.clone()
    projector.unprojectVector(vector, camera)
    raycaster.set(camera.position, vector.sub(camera.position).normalize())
    
    intersects = raycaster.intersectObjects(scene.children)

    if len(intersects) > 0:
        if INTERSECTED != intersects[0].object:
            if INTERSECTED:
                INTERSECTED.material.emissive.setHex(currentHex)
            INTERSECTED = intersects[0].object
            currentHex = INTERSECTED.material.emissive.getHex()
            INTERSECTED.material.emissive.setHex(0xFF0000)
    else:
        if INTERSECTED:
            INTERSECTED.material.emissive.setHex(currentHex)
        INTERSECTED = None

    renderer.render(scene, camera)
    space2D.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench.setUp()
    workbench2D.setUp()
    document.addEventListener("mousemove", onDocumentMouseMove, False)

def tearDown():
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    workbench2D.tearDown()
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
