from three import *
from geometry import *
from browser import *
from workbench import *
from math import pi, exp

space = CartesianSpace()
timeOut = 10

i = VectorE3(1.0, 0.0, 0.0, False)
j = VectorE3(0.0, 1.0, 0.0, False)
k = VectorE3(0.0, 0.0, 1.0, False)

e1 = ArrowBuilder().color(0xFF0000).axis(i).build()#.attitude(exp(-BivectorE3( 0,  0, 1)*pi/4)).build()
e2 = ArrowBuilder().color(0x00FF00).axis(j).build()#.attitude(exp(-BivectorE3( 0, -1, 0)*pi/4)).build()
e3 = ArrowBuilder().color(0x0000FF).axis(k).build()#.attitude(exp(-BivectorE3( 1,  0, 0)*pi/4)).build()

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
    
    space.camera.position.set(2.0, 2.0, 2.0)
    space.camera.lookAt(VectorE3(0.0, 0.0, 0.0))

    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(t):
    space.render()
    
def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
