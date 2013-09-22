from easel import *
from browser import *

def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)

discardCanvases()

canvas = document.createElement("canvas")
canvas.width = 500
canvas.height = 200
container = document.getElementById("canvas-container")
container.appendChild(canvas)

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

circle.addEventListener("click", handleMouseEvent)
circle.addEventListener("dblclick", handleMouseEvent)
circle.addEventListener("mouseover", handleMouseEvent)
circle.addEventListener("mouseout", handleMouseEvent)

square.addEventListener("click", handleMouseEvent)
square.addEventListener("dblclick", handleMouseEvent)
square.addEventListener("mouseover", handleMouseEvent)
square.addEventListener("mouseout", handleMouseEvent)

stage.update()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()