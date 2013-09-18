from three import *
from geometry import *
from browser import *
from math import pi

space = CartesianSpace()
timeOut = 5000

e1 = ArrowBuilder().color(0xFF0000).axis(Vector3(1,0,0)).build()
e2 = ArrowBuilder().color(0x00FF00).axis(Vector3(0,1,0)).build()
e3 = ArrowBuilder().color(0x0000FF).build()

workbench = Workbench(space.renderer, space.camera)

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

def setUp():
    workbench.setUp()

    space.add(e1)
    space.add(e2)
    space.add(e3)
    
    space.camera.position.set(2,2,2)
    space.camera.lookAt(Vector3(0,0,0))

    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()