from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *
from geometry import *

class SphericalPolar:
    def __init__(self):
        self.theta = 0.0
        self.phi = 0.0
    def __str__(self):
        return "(" + str(self.theta) + ", " + str(self.phi) + ")"

origin = VectorE3(0.0, 0.0, 0.0, False)
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
color = "white"
colorB = "#7014CC" # Purple Heart
colorS = "#19FF65" # Spring Green
colorR = "#FF9900" # Orange Peel
colorG = "#999999" # Light Gray

output = Text("Press arrow keys to rotate the qubit. Hit Esc key to exit.", font, "#000000")
output.x = 100
output.y = 60
space2D.addChild(output)

txtCoords = Text("", font, color)
txtCoords.x = 100
txtCoords.y = 100
space2D.addChild(txtCoords)

txtRotor = Text("", font, colorR)
txtRotor.x = 100
txtRotor.y = 130
space2D.addChild(txtRotor)

txtProjection = Text("", font, colorR)
txtProjection.x = 100
txtProjection.y = 160
space2D.addChild(txtProjection)

txtBloch = Text("", font, colorB)
txtBloch.x = 100
txtBloch.y = 190
space2D.addChild(txtBloch)

txtSpinor = Text("", font, color)
txtSpinor.x = 100
txtSpinor.y = 210
space2D.addChild(txtSpinor)

txtException = Text("", font, "red")
txtException.x = 100
txtException.y = 240
space2D.addChild(txtException)

timeOut = 6000.0

isShiftDown = False
isCtrlDown = False

space3D = CartesianSpace()

probeN = ProbeBuilderE3().color(colorB).build()
space3D.add(probeN.grade0)
space3D.add(probeN.grade1)
space3D.add(probeN.grade2)
space3D.add(probeN.grade3)
probeN.position = e1 - e2

probeR0 = ProbeBuilderE3().color(colorR).wireframe(False).build()
space3D.add(probeR0.grade0)
probeR0.position = e2 - e1

probeR2 = ProbeBuilderE3().color(colorR).build()
space3D.add(probeR2.grade2)
probeR2.position = VectorE3(0.0, 0.0, 0.0)

probeE1 = ProbeBuilderE3().color("#FF0000").build()
space3D.add(probeE1.grade1)
probeE1.position = origin

probeE2 = ProbeBuilderE3().color("#00FF00").build()
space3D.add(probeE2.grade1)
probeE2.position = origin

probeE3 = ProbeBuilderE3().color("#0000FF").build()
space3D.add(probeE3.grade1)
probeE3.position = origin

space3D.renderer.setClearColor(0x777777, 1.0)
space3D.camera.position = (4 * e1 + 4 * e2 + 2 * e3) * 0.6
space3D.camera.lookAt(probeR2.position)

workbench = Workbench3D(space3D.renderer.domElement, space3D.renderer, space3D.camera)

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
        coords.phi = min(coords.phi, 720.0)

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
    theta = radians(coords.theta)
    phi = radians(coords.phi)
    
    txtCoords.text = "Spherical polar coordinates (theta, phi):" + str(coords) + " degrees."
    R = exp(- I * e3 * phi / 2) * exp(- I * e2 * theta / 2)
    n = sin(theta) * (cos(phi) * e1 + sin(phi) * e2) + cos(theta) * e3 # R * e3 * ~R
    
    txtRotor.text = "Rotor, R = " + str(R)
    txtProjection.text = "Projection of 1 and e1 ^ e2 components, (R + e3 * R * e3) / 2.0 = " + str((R + e3 * R * e3) / 2.0)
    
    txtBloch.text = "Bloch sphere unit vector, n = R * e3 * ~R = " + str(n)
    
    probeR0.quantity = R
    probeR2.quantity = R
    probeN.quantity = n
    
    probeE1.quantity = R * e1 * ~R
    probeE2.quantity = R * e2 * ~R
    probeE3.quantity = R * e3 * ~R
    
    space3D.render()
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

def tearDown(e):
    document.removeEventListener("mousedown", onDocumentMouseDown, False)
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("mouseup",   onDocumentMouseUp, False)
    document.removeEventListener("mouseout",  onDocumentMouseOut, False)
    document.removeEventListener("keyup",     onDocumentKeyUp, False)
    document.removeEventListener("keydown",   onDocumentKeyDown, False)
    workbench2D.tearDown()
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(render, terminate, setUp, tearDown, window).start()
