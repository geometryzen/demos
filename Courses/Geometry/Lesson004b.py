from browser import WindowAnimationRunner, document
from geometry import CartesianSpace, ArrowBuilder, ProbeBuilderE3
from workbench import Workbench
from e3ga import *
from math import exp, sqrt, pi

f = VectorE3(3.0, -2.0, 0.0)
g = VectorE3(0.0, 2.0, 0.0)
h = VectorE3(1.0, 1.0, 0.0)

scene = CartesianSpace()

def magnitude(v):
    return sqrt(v.x * v.x + v.y * v.y)

def attitude(v):
    a = VectorE3(0, 0, 1)
    b = VectorE3(v.x, v.y, 0) / magnitude(v)
    numer = 1 + b * a
    denom = ScalarE3(sqrt(2 + (a % b)))
    R = numer / denom
    return R

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
        f = f + Vector(0.0, -0.1)
    if moveRight:
        f = f + Vector(0.0, +0.1)
    if moveForward:
        f = f + Vector(-0.1, 0.0)
    if moveBackward:
        f = f + Vector(+0.1, 0.0)
    u = f + g
    v = g + h
    probeR.quantity = VectorE3(f.x, f.y, 0)
    probeR.grade1.position.set(f.x / 2.0, f.y / 2.0, 0.0)
    probeG.quantity = VectorE3(g.x, g.y, 0)
    probeG.grade1.position.set(g.x / 2.0 + f.x, g.y / 2.0 + f.y, 0.0)
    probeB.quantity = VectorE3(h.x, h.y, 0)
    probeB.grade1.position.set(h.x / 2.0 + u.x, h.y / 2.0 + u.y, 0.0)
    probeY.quantity = VectorE3(u.x, u.y, 0)
    probeY.grade1.position.set(u.x / 2.0, u.y / 2.0, 0.0)
    probeC.quantity = VectorE3(v.x, v.y, 0)
    probeC.grade1.position.set(v.x / 2.0 + f.x, v.y / 2.0 + f.y, 0.0)
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
