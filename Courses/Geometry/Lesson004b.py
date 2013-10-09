from browser import WindowAnimationRunner, document
from geometry import CartesianSpace, ArrowBuilder, ProbeBuilderE3
from workbench import Workbench
from e3ga import *
from math import exp, sqrt, pi

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)

f = 3 * i - 2 * j
g = 2 * j
h = i + j

scene = CartesianSpace()

probeR = ProbeBuilderE3().color("red").build()
scene.add(probeR.grade1)

probeG = ProbeBuilderE3().color("green").build()
scene.add(probeG.grade1)

probeB = ProbeBuilderE3().color("blue").build()
scene.add(probeB.grade1)

probeY = ProbeBuilderE3().color("yellow").build()
scene.add(probeY.grade1)

probeC = ProbeBuilderE3().color("cyan").build()
scene.add(probeC.grade1)

workbench = Workbench(scene.renderer, scene.camera)

timeOut = 30

moveLeft = False
moveForward = False
moveRight = False
moveBackward = False

def escKey(event, downFlag):
    event.preventDefault()
    global timeOut
    timeOut = 0

def leftArrowKey(event, downFlag):
    event.preventDefault()
    global moveLeft
    moveLeft = downFlag

def upArrowKey(event, downFlag):
    event.preventDefault()
    global moveForward
    moveForward = downFlag
    
def rightArrowKey(event, downFlag):
    event.preventDefault()
    global moveRight
    moveRight = downFlag

def downArrowKey(event, downFlag):
    event.preventDefault()
    global moveBackward
    moveBackward = downFlag

keyHandlers = {
 27: escKey,
 37: leftArrowKey,
 38: upArrowKey,
 39: rightArrowKey,
 40: downArrowKey
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

def tick(t):
    global f
    if moveLeft:
        f -= 0.1 * i
    if moveRight:
        f = f + VectorE3(0.0, +0.1, 0.0)
    if moveForward:
        f = f + VectorE3(-0.1, 0.0, 0.0)
    if moveBackward:
        f = f + VectorE3(+0.1, 0.0, 0.0)
        
    u = f + g
    v = g + h
    
    probeR.quantity = f
    probeR.grade1.position = f / 2
    
    probeG.quantity = g
    probeG.grade1.position = g / 2 + f
    
    probeB.quantity = h
    probeB.grade1.position = h / 2 + u
    
    probeY.quantity = u
    probeY.grade1.position = u / 2
    
    probeC.quantity = v
    probeC.grade1.position = v / 2 + f
    
    scene.render()

def terminate(t):
    done = t > timeOut
    return done

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup",   onDocumentKeyUp, False)

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup",   onDocumentKeyUp, False)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
