'''
This program may not work for you because I am working on it right now!
'''
from geometry import *
from browser import *

space = CartesianSpace()

shape = ArrowBuilder().color(0xFFFF00).build()
space.add(shape)

workbench = Workbench(space.renderer, space.camera)

timeOut = 6

def onDocumentKeyDown(event):
    global timeOut
    if event.keyCode == 27:
        timeOut = 0

def setUp():
    space.camera.position.set(1.5, 1.5, 1.5)
    space.camera.lookAt(space.origin)
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(t):
    space.render()
    
def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()
    
WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
