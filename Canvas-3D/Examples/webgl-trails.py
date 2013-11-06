'''
Under Construction
'''
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

timeOut = 6000.0

mouse = VectorE3(0, 10000, 0.5)

isShiftDown = False
isCtrlDown = False

scene = Scene()
renderer = None

camera = PerspectiveCamera(60, 1, 1, 10000)
camera.position.set(10000, 0, 3200)

workbench = None

def shiftKey(event, downFlag):
    global isShiftDown
    isShiftDown = downFlag

def ctrlKey(event, downFlag):
    global isCtrlDown
    isCtrlDown = downFlag
    
def escKey(event, downFlag):
    event.preventDefault()
    global timeOut
    timeOut = 0

keyHandlers = {
 16: shiftKey,
 17: ctrlKey, 
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
    event.preventDefault()
    mouse.x = (float(event.clientX) / float(window.innerWidth)) * 2.0 - 1.0
    mouse.y = - (float(event.clientY) / float(window.innerHeight)) * 2.0 + 1.0

def tick(t):

    camera.position.x += (+mouse.x - camera.position.x) * 0.05
    camera.position.y += (-mouse.y - camera.position.y) * 0.05
    camera.lookAt(scene.position)
    
    renderer.render(scene, camera)
    space2D.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    global renderer, workbench
    colors = [0x000000,0xFF0080,0x8000FF, 0xFFFFFF]
    geometry = Geometry()
    for i in range(0, 2000):
        vertex = VectorE3(0.0, 0.0, 0.0)
        vertex.x = random() * 4000.0 - 2000.0
        vertex.y = random() * 4000.0 - 2000.0
        vertex.z = random() * 4000.0 - 2000.0
        geometry.vertices.append(vertex)
        geometry.colors.append(Color(colors[floor(random() * len(colors))]))
        
    material = ParticleSystemMaterial({"size": 1, "vertexColors": VertexColors, "depthTest": False, "opacity": 0.5, "sizeAttenuation": False, "transparent": True})
    
    mesh = ParticleSystem(geometry, material)
    scene.add(mesh)

    renderer = WebGLRenderer({"preserveDrawingBuffer": True})
    renderer.sortObjects = False
    renderer.autoClearColor = False
    renderer.setClearColor(0x000000, 1.0)

    workbench = Workbench(renderer, camera)

    workbench.setUp()
    workbench2D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)
    document.addEventListener("mousemove", onDocumentMouseMove, False)

def tearDown():
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench2D.tearDown()
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
