'''
This program may not work for you because I am working on it right now!
'''
from geometry import *
from browser import *

space = CartesianSpace()

shape = ArrowBuilder().color(0xFFFF00).build()
space.add(shape)

workbench = Workbench(space.renderer, space.camera)

timeOut = 6000

def onDocumentKeyDown(event):
    global timeOut
    if event.keyCode == 27:
        timeOut = 0

def setUp():
    # TODO: Need to fix the entire graphics API now we are moving from Vector3, Quaternion to Euclidean3.
#    space.camera.position.set(1.5, 1.5, 1.5)
    space.camera.lookAt()#space.origin)
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()
    
WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
