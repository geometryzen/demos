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
print repr(canvas)
container.appendChild(canvas)

stage = Stage(canvas)
circle = Shape()
circle.graphics.beginFill("red").drawCircle(0, 0, 50)
circle.x = 100
circle.y = 100
stage.addChild(circle)

def handleTick():
    circle.x += 10
    if (circle.x > canvas.width):
        circle.x = 0
    stage.update()

Ticker.addEventListener("tick", handleTick)