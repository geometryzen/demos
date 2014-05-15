from three import *
from browser import *
from workbench import *
from random import random
from math import *

timeOut = 10.0

mouse = VectorE3(0.0, 0.0, 0.0)

scene = Scene()

camera = PerspectiveCamera(60, 1, 1, 10000)
camera.position.set(10000.0, 0.0, 3200.0)

colors = [0x000000,0xFF0080,0x8000FF, 0xFFFFFF]
geometry = Geometry()
for i in range(0, 2000):
    vertex = VectorE3(0.0, 0.0, 0.0)
    vertex.x = random() * 4000.0 - 2000.0
    vertex.y = random() * 4000.0 - 2000.0
    vertex.z = random() * 4000.0 - 2000.0
    geometry.vertices.append(vertex)
    geometry.colors.append(Color(colors[floor(random() * len(colors))]))
    
material = ParticleSystemMaterial({"size": 1.0, "vertexColors": VertexColors, "depthTest": False, "opacity": 0.5, "sizeAttenuation": False, "transparent": True})
    
mesh = ParticleSystem(geometry, material)
scene.add(mesh)
    
renderer = WebGLRenderer({"preserveDrawingBuffer": True})
renderer.sortObjects = False
renderer.autoClearColor = False
renderer.setClearColor(0x000000, 1.0)

workbench = Workbench3D(renderer.domElement, renderer, camera)

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
    document.addEventListener("mousemove", onDocumentMouseMove, False)

def tearDown():
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
