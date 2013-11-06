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
renderer = WebGLRenderer({"preserveDrawingBuffer":True})

camera = PerspectiveCamera(70, 1, 1, 10000)
camera.position.y = 800

workbench = Workbench(renderer, camera)

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

def onDocumentMouseDown(event):
    event.preventDefault()

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
    geometry = Geometry()
    size = 500
    step = 50
    for i in range(-size, size + 1, step):
        geometry.vertices.append(VectorE3(-size, 0, i))
        geometry.vertices.append(VectorE3(+size, 0, i))
        geometry.vertices.append(VectorE3(i, 0, -size))
        geometry.vertices.append(VectorE3(i, 0, +size))

    material = LineBasicMaterial({"color": 0x000000, "opacity": 0.2})
    line = Line(geometry, material, LinePieces)
    scene.add(line)
    
    plane.rotation.x = - pi / 2.0
    plane.visible = False
    scene.add(plane)
    
    workbench.setUp()
    workbench2D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)
    document.addEventListener("mousemove", onDocumentMouseMove, False)
    document.addEventListener("mousedown", onDocumentMouseDown, False)

def tearDown():
    document.removeEventListener("mousedown", onDocumentMouseDown, False)
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench2D.tearDown()
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
