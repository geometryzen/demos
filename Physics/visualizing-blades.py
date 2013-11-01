from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *
from math import exp, pi

A = e1 * e2
B = e2
C = A * B

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

output = Text("Hit Esc key to exit.", "20px Helvetica", "white")
output.x = 100
output.y = 100
space2D.addChild(output)

outputA = Text("", "20px Helvetica", "red")
outputA.x = 100
outputA.y = 120
space2D.addChild(outputA)

outputOp = Text("*", "20px Helvetica", "white")
outputOp.x = 100
outputOp.y = 140
space2D.addChild(outputOp)

outputB = Text("", "20px Helvetica", "green")
outputB.x = 100
outputB.y = 160
space2D.addChild(outputB)

outputEq = Text("=", "20px Helvetica", "white")
outputEq.x = 100
outputEq.y = 180
space2D.addChild(outputEq)

outputC = Text("", "20px Helvetica", "blue")
outputC.x = 100
outputC.y = 200
space2D.addChild(outputC)

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
    outputA.text = str(A)
    outputB.text = str(B)
    outputC.text = str(C)
    space3D.render()
    space2D.render()

def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
