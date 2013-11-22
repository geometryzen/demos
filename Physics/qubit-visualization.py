from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *

e1 = VectorE3(1.0, 0.0, 0.0, False)
e2 = VectorE3(0.0, 1.0, 0.0, False)
e3 = VectorE3(0.0, 0.0, 1.0, False)

projector = Projector()
raycaster = None

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text("Drag to spin the qubit. Hit Esc key to exit.", font, "#FFFF00")
output.x = 100
output.y = 60
space2D.addChild(output)

txtSpinor = Text("", font, "black")
txtSpinor.x = 100
txtSpinor.y = 120
space2D.addChild(txtSpinor)

txtMouseDown = Text("", font, "black")
txtMouseDown.x = 100
txtMouseDown.y = 140
space2D.addChild(txtMouseDown)

txtScratch = Text("", font, "black")
txtScratch.x = 100
txtScratch.y = 300
space2D.addChild(txtScratch)

timeOut = 6000.0

mouse = VectorE3(0.0, 0.0, 0.0)
mouseOnMouseDown = VectorE3(0.0, 0.0, 0.0)
targetRotation = 0
targetRotationOnMouseDown = 0
isShiftDown = False
isCtrlDown = False

camera = PerspectiveCamera(70, 1, 1, 10000)
camera.position.x = 2
camera.position.y = 0
camera.position.z = 1.5

scene = Scene()

geometry = CubeGeometry(1.0, 1.0, 1.0)
faces = geometry.faces
faces[0].color.setHex(0xFF0000)
faces[1].color.setHex(0xFF0000)
faces[2].color.setHex(0x00FFFF)
faces[3].color.setHex(0x00FFFF)
faces[4].color.setHex(0x00FF00)
faces[5].color.setHex(0x00FF00)
faces[6].color.setHex(0xFF00FF)
faces[7].color.setHex(0xFF00FF)
faces[8].color.setHex(0x0000FF)
faces[9].color.setHex(0x0000FF)
faces[10].color.setHex(0xFFFF00)
faces[11].color.setHex(0xFFFF00)
    
material = MeshBasicMaterial({"vertexColors": FaceColors, "overdraw": 0.5})
cube = Mesh(geometry, material)
scene.add(cube)

geometry = SphereGeometry(1.0, 24, 24)
material = MeshBasicMaterial({"wireframe": True, "wireframeLinewidth": 1, "color": Color(0xFFFFFF)})
sphere = Mesh(geometry, material)
scene.add(sphere)

camera.up = e3
camera.lookAt(cube.position)

renderer = CanvasRenderer()
renderer.setClearColor(0x777777, 1.0)

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
    
def deviceX(clientX):
    return 2.0 * (float(clientX) / float(window.innerWidth)) - 1.0

def deviceY(clientY):
    return 1.0 - 2.0 * (float(clientY) / float(window.innerHeight))

def onDocumentMouseDown(event):

    event.preventDefault()

    document.addEventListener("mousemove", onDocumentMouseMove, False)
    document.addEventListener("mouseup", onDocumentMouseUp, False)
    document.addEventListener("mouseout", onDocumentMouseOut, False)
    
    intersects = raycaster.intersectObjects(scene.children)
    if len(intersects) > 0:
        intersect = intersect[0]
        txtScratch.text = intersect
    
def onDocumentMouseMove(event):
    mouse.x = deviceX(event.clientX)
    mouse.y = deviceY(event.clientY)

def onDocumentMouseUp(event):
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("mouseup", onDocumentMouseUp, False)
    document.removeEventListener("mouseout", onDocumentMouseOut, False)

def onDocumentMouseOut(event):
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("mouseup", onDocumentMouseUp, False)
    document.removeEventListener("mouseout", onDocumentMouseOut, False)
        
def render(t):
    raycaster = projector.pickingRay(mouse.clone(), camera)
    txtScratch.text = raycaster
    cube.rotation.z += (targetRotation - cube.rotation.z) * 0.05
    sphere.rotation.z += (targetRotation - sphere.rotation.z) * 0.05
    txtSpinor.text = mouse
    txtMouseDown.text = mouseOnMouseDown

    renderer.render(scene, camera)
    space2D.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench.setUp()
    workbench2D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)
    document.addEventListener("mousedown", onDocumentMouseDown, False)

def tearDown():
    document.removeEventListener("mousedown", onDocumentMouseDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench2D.tearDown()
    workbench.tearDown()

WindowAnimationRunner(render, terminate, setUp, tearDown).start()
