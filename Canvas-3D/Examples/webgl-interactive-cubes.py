'''
Under Construction. Nov 3, 2013
'''
from three import *
from browser import *
from workbench import *
from random import random
from math import *

radius = 100.0
omega  = 2.0 * pi / 20.0
timeOut = 60.0

mouse = VectorE3(0.0, 0.0, 1.0)
INTERSECTED = None

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

projector = Projector()
raycaster = Raycaster()

geometry = CubeGeometry(20, 20, 20)

for i in range(0, 20):
    object = Mesh(geometry, MeshLambertMaterial({"color": random() * 0xFFFFFF}))
    object.position.x = random() * 800.0 - 400.0
    object.position.y = random() * 800.0 - 400.0
    object.position.z = random() * 800.0 - 400.0
    
    object.rotation.x = random() * 2.0 * pi
    object.rotation.y = random() * 2.0 * pi
    object.rotation.z = random() * 2.0 * pi
    
    object.scale.x = random() + 0.5
    object.scale.y = random() + 0.5
    object.scale.z = random() + 0.5
    
    scene.add(object)
    
workbench = Workbench(renderer, camera)

def escKey(event, downFlag):
    event.preventDefault()
    global timeOut
    timeOut = 0

keyHandlers = {
 27: escKey
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except:
        pass

def onDocumentMouseMove(event):
    event.preventDefault()
    mouse.x = (float(event.clientX) / float(window.innerWidth)) * 2.0 - 1.0
    mouse.y = (float(event.clientY) / float(window.innerHeight)) * 2.0 + 1.0

def tick(t):
    theta = omega * t
    camera.position.x = radius * sin(theta)
    camera.position.y = radius * sin(theta)
    camera.position.z = radius * cos(theta)
    camera.lookAt(scene.position)
    
    vector = mouse.clone()
    projector.unprojectVector(vector, camera)
    raycaster.set(camera.position, vector.sub(camera.position).normalize())
    
    intersects = raycaster.intersectObjects(scene.children)
    print len(intersects)
    if len(intersects) > 0:
        if INTERSECTED != intersects[0].object:
            if INTERSECTED:
                print INTERSECTED

    renderer.render(scene, camera)
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("mousemove", onDocumentMouseMove, False)

def tearDown():
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
