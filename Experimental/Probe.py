from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *
from math import exp, pi

timeOut = 60

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

output = Text("", "20px Helvetica", "white")
output.x = window.innerWidth / 2
output.y = window.innerHeight / 2
space2D.addChild(output)

quantity = ScalarE3(1) + VectorE3(2, 4, 0) + BivectorE3(5,0,0) + PseudoscalarE3(8)

# Define the Meshes that you want to represent each grade of the quantity.
grade0 = SphereBuilder().wireframe(True).color(0x808080).segments(12).build()
grade1 = ArrowBuilder().color(0x808080).wireframe(True).segments(12).build()
grade2 = PlaneBuilder().wireframe(True).color(0xFFFFFF).segments(5).build()
grade3 = CubeBuilder().wireframe(True).color(0xFFFFFF).segments(1).build()

probe  = ProbeE3(grade0, grade1, grade2, grade3)

space3D.add(probe.grade0)
space3D.add(probe.grade1)
space3D.add(probe.grade2)
space3D.add(probe.grade3)

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
    probe.quantity = quantity
    output.text = repr(probe.quantity)
    space3D.render()
    space2D.update()

def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
