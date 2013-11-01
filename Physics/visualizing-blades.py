from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *
from math import exp, pi

timeOut = 20

space3D = CartesianSpace()
canvas3D = space3D.renderer.domElement
workbench3D = Workbench3D(canvas3D, space3D.renderer, space3D.camera)
   
canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

outputA = Text("", "20px Helvetica", 0xFF0000)
outputA.x = 100
outputA.y = 100
space2D.addChild(outputA)

A = e1
B = e2
C = A * B

probeA  = ProbeBuilderE3().color(0xFF0000).build()
space3D.add(probeA.grade0)
space3D.add(probeA.grade1)
space3D.add(probeA.grade2)
space3D.add(probeA.grade3)
probeB  = ProbeBuilderE3().color(0x00FF00).build()
space3D.add(probeB.grade0)
space3D.add(probeB.grade1)
space3D.add(probeB.grade2)
space3D.add(probeB.grade3)
probeC  = ProbeBuilderE3().color(0x0000FF).build()
space3D.add(probeC.grade0)
space3D.add(probeC.grade1)
space3D.add(probeC.grade2)
space3D.add(probeC.grade3)

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
    workbench2D.setUp()
    workbench3D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(t):
    probeA.quantity = A
    probeB.quantity = B
    probeC.quantity = C
    outputA.text = str(probeA.quantity)
    space3D.render()
    space2D.render()

def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
