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

arrow = ArrowBuilder().build()
space3D.add(arrow)

output = Text("", "20px Helvetica", "white")
output.x = window.innerWidth / 2
output.y = window.innerHeight / 2
space2D.addChild(output)

square = Shape()
square.graphics.beginFill("black").drawRoundRect(0, 0, 100, 40, 6).endFill()
square.graphics.beginStroke("white").drawRoundRect(0, 0, 100, 40, 6).endStroke()
square.x = 200
square.y = 100
square.name = "square"
space2D.addChild(square)

quantity = VectorE3(0, 0, 3)

def handleMouseEvent(event):
    quantity.x += 0.1

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()
    square.addEventListener("click", handleMouseEvent)

def tick(t):
    m = quantity.length()
    arrow.scale = VectorE3(m, m, m)
    space3D.render()
    space2D.update()
    output.text = repr(quantity)

def terminate(t):
    return t > 10

def tearDown():
    square.removeEventListener("click", handleMouseEvent)
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()