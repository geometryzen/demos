from easel import *
from browser import *
from workbench import *

canvas = document.createElement("canvas")

stage = Stage(canvas)
stage.enableMouseOver()

output = Text("Mouse Events Demonstration", "14px Arial")
output.x = output.y = 10
stage.addChild(output)

circle = Shape()
circle.graphics.beginFill("red").drawCircle(0, 0, 50).endFill()
circle.x = circle.y = 100
circle.name = "circle"
stage.addChild(circle)

square = Shape()
square.graphics.beginFill("green").drawRect(-50, -50, 100, 100).endFill()
square.x = 250
square.y = 100
square.name = "square"
stage.addChild(square)

def handleMouseEvent(event):
    output.text = str({"target": event.target, "type": event.type})
    stage.update()

workbench = Workbench2D(canvas)

def setUp():
    workbench.setUp()
    circle.addEventListener("click", handleMouseEvent)
    circle.addEventListener("dblclick", handleMouseEvent)
    circle.addEventListener("mouseover", handleMouseEvent)
    circle.addEventListener("mouseout", handleMouseEvent)

    square.addEventListener("click", handleMouseEvent)
    square.addEventListener("dblclick", handleMouseEvent)
    square.addEventListener("mouseover", handleMouseEvent)
    square.addEventListener("mouseout", handleMouseEvent)

def tick(t):
    stage.update()

def terminate(t):
    return t > 6

def tearDown():
    circle.removeEventListener("click", handleMouseEvent)
    circle.removeEventListener("dblclick", handleMouseEvent)
    circle.removeEventListener("mouseover", handleMouseEvent)
    circle.removeEventListener("mouseout", handleMouseEvent)

    square.removeEventListener("click", handleMouseEvent)
    square.removeEventListener("dblclick", handleMouseEvent)
    square.removeEventListener("mouseover", handleMouseEvent)
    square.removeEventListener("mouseout", handleMouseEvent)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
