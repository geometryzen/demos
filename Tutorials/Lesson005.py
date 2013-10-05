from browser import document, WindowAnimationRunner
from geometry import CartesianSpace, SphereBuilder
from math import cos, sin, pi
from workbench import Workbench

T = 5
omega = 2 * pi / T
R = 4

space = CartesianSpace()

sphere = SphereBuilder().color(0x0000FF).build()
space.add(sphere)

workbench = Workbench(space.renderer, space.camera)

timeOut = 20

def tick(t):
    sphere.position.set(R * cos(omega*t), R * sin(omega*t), 0)
    space.render()

def terminate(t):
    done = t > 20
    return done

def setUp():
    document.addEventListener("keydown", onDocumentKeyDown, False)
    workbench.setUp()

def tearDown():
    workbench.tearDown()
    
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

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()