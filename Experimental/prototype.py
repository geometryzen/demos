from browser import *
from geometry import *
from math import *
from workbench import *

T = 5 # Periodic Time
omega = 2 * pi / T # Angular Velocity
R = 4 # radius

container = document.getElementById("canvas-container")
canvas = document.createElement("canvas")
# There is a bug in Chrome (up to version 29) that stops this from working...
container.appendChild(canvas)

space = CartesianSpace()

sphere = SphereBuilder().color(0x0000FF).build()
space.add(sphere)

workbench = Workbench(space.renderer, space.camera)

timeOut = 1.5 * T

def tick(t):
    sphere.position.set(R * cos(omega*t), R * sin(omega*t), 0)
    space.render()

def terminate(time):
    return time > timeOut

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

def escKey(event, downFlag):
    event.preventDefault()
    global timeOut
    timeOut = 0

keyHandlers = {27: escKey}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except:
        pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
