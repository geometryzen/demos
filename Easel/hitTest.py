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
circle = stage.addChild(Shape())
circle.graphics.beginFill("red").drawCircle(50, 50, 50)
circle.x = 0
circle.y = 0

def tick():
    circle.alpha = 0.2
    if (circle.hitTest(stage.mouseX, stage.mouseY)):
        circle.alpha = 1
    stage.update()

Ticker.addEventListener("tick", tick)