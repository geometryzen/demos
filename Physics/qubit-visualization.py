'''
Under Construction. Nov 22, 2013.
'''
from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *

class SphericalPolar:
    def __init__(self):
        self.theta = 0.0
        self.phi = 0.0
    def __str__(self):
        return "(" + str(self.theta) + ", " + str(self.phi) + ")"

e1 = VectorE3(1.0, 0.0, 0.0, False)
e2 = VectorE3(0.0, 1.0, 0.0, False)
e3 = VectorE3(0.0, 0.0, 1.0, False)
I = e1 ^ e2 ^ e3

coords = SphericalPolar()

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text("Press arrow keys to rotate the qubit. Hit Esc key to exit.", font, "#FFFF00")
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

txtException = Text("", font, "red")
txtException.x = 100
txtException.y = 200
space2D.addChild(txtException)

timeOut = 6000.0

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

camera.up = e3
camera.lookAt(scene.position)

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

def arrowLeft(event, downFlag):
    event.preventDefault()
    if downFlag:
        coords.phi -= 1.0
        coords.phi = max(coords.phi, 0.0)

def arrowRight(event, downFlag):
    event.preventDefault()
    if downFlag:
        coords.phi += 1.0
        coords.phi = min(coords.phi, 360.0)

def arrowUp(event, downFlag):
    event.preventDefault()
    if downFlag:
        coords.theta -= 1.0
        coords.theta = max(coords.theta, 0.0)

def arrowDown(event, downFlag):
    event.preventDefault()
    if downFlag:
        coords.theta += 1.0
        coords.theta = min(coords.theta, 180.0)

keyHandlers = {
 16: shiftKey,
 17: ctrlKey, 
 27: escKey,
 37: arrowLeft,
 38: arrowUp,
 39: arrowRight,
 40: arrowDown
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except KeyError as keyError:
        pass
    except Exception as e:
        txtException.text = e

def onDocumentKeyUp(event):
    try:
        keyHandlers[event.keyCode](event, False)
    except KeyError as keyError:
        pass
    except Exception as e:
        txtException.text = e
    
def deviceX(clientX):
    return 2.0 * (float(clientX) / float(window.innerWidth)) - 1.0

def deviceY(clientY):
    return 1.0 - 2.0 * (float(clientY) / float(window.innerHeight))

def onDocumentMouseDown(event):
    event.preventDefault()
    
def onDocumentMouseMove(event):
    mouse.x = deviceX(event.clientX)
    mouse.y = deviceY(event.clientY)

def onDocumentMouseUp(event):
    pass

def onDocumentMouseOut(event):
    pass
        
def render(t):
    R = exp(- I * e3 * radians(coords.phi) / 2) * exp(- I * e2 * radians(coords.theta) / 2)
    txtScratch.text = R
    cube.attitude = R
    renderer.render(scene, camera)
    space2D.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench.setUp()
    workbench2D.setUp()
    document.addEventListener("keydown",   onDocumentKeyDown, False)
    document.addEventListener("keyup",     onDocumentKeyUp, False)
    document.addEventListener("mousedown", onDocumentMouseDown, False)
    document.addEventListener("mousemove", onDocumentMouseMove, False)
    document.addEventListener("mouseup",   onDocumentMouseUp, False)
    document.addEventListener("mouseout",  onDocumentMouseOut, False)

def tearDown():
    document.removeEventListener("mousedown", onDocumentMouseDown, False)
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("mouseup",   onDocumentMouseUp, False)
    document.removeEventListener("mouseout",  onDocumentMouseOut, False)
    document.removeEventListener("keyup",     onDocumentKeyUp, False)
    document.removeEventListener("keydown",   onDocumentKeyDown, False)
    workbench2D.tearDown()
    workbench.tearDown()

WindowAnimationRunner(render, terminate, setUp, tearDown).start()
