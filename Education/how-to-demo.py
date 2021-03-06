from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *
from math import *

done = False

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

arrow = ArrowBuilder().segments(12).build()
space3D.add(arrow)

output = Text("", "20px Helvetica", "white")
output.x = window.innerWidth / 2
output.y = window.innerHeight / 2
space2D.addChild(output)

exit = Shape()
exit.graphics.beginFill("black").drawRoundRect(0, 0, 40, 40, 6).endFill()
exit.graphics.beginStroke("white").drawRoundRect(0, 0, 40, 40, 6).endStroke()
exit.x = 200
exit.y = 50
exit.name = "square"
space2D.addChild(exit)
exitText = Text("Exit", "9pt Helvetica", "white")
exitText.x = exit.x + 10
exitText.y = exit.y + 12
space2D.addChild(exitText)

square = Shape()
square.graphics.beginFill("black").drawRoundRect(0, 0, 40, 40, 6).endFill()
square.graphics.beginStroke("white").drawRoundRect(0, 0, 40, 40, 6).endStroke()
square.x = 200
square.y = 100
square.name = "square"
space2D.addChild(square)

quantity = VectorE3(0.0, 3.0, 0.0)

def handleMouseEvent(event):
    quantity.y += 0.1

def onClickExit(event):
    global done
    done = True

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()
    square.addEventListener("click", handleMouseEvent)
    exit.addEventListener("click", onClickExit)

def tick(t):
    m = sqrt(quantity.magnitude())
    arrow.scale = VectorE3(m, m, m)
    output.text = repr(quantity)

    space3D.render()
    space2D.render()

def terminate(t):
    return done

def tearDown():
    exit.removeEventListener("click", onClickExit)
    square.removeEventListener("click", handleMouseEvent)
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()