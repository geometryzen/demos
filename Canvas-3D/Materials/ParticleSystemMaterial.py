'''
Under Construction. Nov 6, 2013
'''
from three import *
from browser import *
from workbench import *
from random import random
from math import *

timeOut = 4.0

mouse = VectorE3(0, 0, 0)

scene = Scene()

camera = PerspectiveCamera(60, 1, 1, 10000)
camera.position.set(10000, 0, 3200)

material = ParticleSystemMaterial({"size": 1.0, "vertexColors": True, "depthTest": False, "opacity": 0.5, "sizeAttenuation": False, "transparent": True})
material.size = 2.0
print material.size
material.color = Color(0x00FF00)
print material.color
material.sizeAttenuation = False
print material.sizeAttenuation
material.vertexColors = False
print material.vertexColors
print material.fog
print material
print repr(material)

colors = [0x000000,0xFF0080,0x8000FF, 0xFFFFFF]
geometry = Geometry()
for i in range(0, 2000):
    vertex = VectorE3(0.0, 0.0, 0.0)
    vertex.x = random() * 4000.0 - 2000.0
    vertex.y = random() * 4000.0 - 2000.0
    vertex.z = random() * 4000.0 - 2000.0
    geometry.vertices.append(vertex)
    geometry.colors.append(Color(colors[floor(random() * len(colors))]))
    
mesh = ParticleSystem(geometry, material)
scene.add(mesh)
    
renderer = WebGLRenderer({"preserveDrawingBuffer": True})
renderer.sortObjects = False
renderer.autoClearColor = False
renderer.setClearColor(0x000000, 1.0)

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

def onDocumentKeyUp(event):
    try:
        keyHandlers[event.keyCode](event, False)
    except:
        pass

def onDocumentMouseMove(event):
    windowHalfX = float(window.innerWidth) / 2.0
    windowHalfY = float(window.innerHeight) / 2.0
    
    mouse.x = (float(event.clientX) - windowHalfX) * 10.0
    mouse.y = (float(event.clientY) - windowHalfY) * 10.0

def tick(t):

    camera.position.x += (+mouse.x - camera.position.x) * 0.05
    camera.position.y += (-mouse.y - camera.position.y) * 0.05

    camera.lookAt(scene.position)
    
    renderer.render(scene, camera)
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)
    document.addEventListener("mousemove", onDocumentMouseMove, False)

def tearDown():
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
