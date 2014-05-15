from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *

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

arrow = ArrowBuilder().scale(3).build()

output = Text("Mouse Events Demonstration", "20px Helvetica", "white")
output.x = window.innerWidth / 2
output.y = window.innerHeight / 2
space2D.addChild(output)

quantity = VectorE3(1.0, 2.0, 3.0)

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()

    space3D.add(arrow)

def tick(t):
    space3D.render()
    space2D.update()
    output.text = str(quantity)

def terminate(t):
    return False

def tearDown(e):
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
