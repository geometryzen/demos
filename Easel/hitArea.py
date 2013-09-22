from easel import *
from browser import *

def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)

def onMouseOver(event):
    event.target.alpha = 1

def onMouseOut(event):
    event.target.alpha = 0.5

discardCanvases()

canvas = document.createElement("canvas")
canvas.width = 400
canvas.height = 300
container = document.getElementById("canvas-container")
container.appendChild(canvas)

stage = Stage(canvas)
stage.enableMouseOver(10)

labelA = Text("A", "bold 48px Arial", "#FF0000")
labelA.x = 10
labelA.y = 10
labelA.alpha = 0.5

labelB = Text("A", "bold 48px Arial", "#0000FF")
labelB.x = 10
labelB.y = 80
labelB.alpha = 0.5

hit = Shape()
w = labelB.getMeasuredWidth()
h = labelB.getMeasuredHeight()
hit.graphics.beginFill("#000000").drawRect(0,0,w,h).endFill()
labelB.hitArea = hit

labelA.addEventListener("mouseover", onMouseOver)
labelB.addEventListener("mouseover", onMouseOver)

labelA.addEventListener("mouseout", onMouseOut)
labelB.addEventListener("mouseout", onMouseOut)

stage.addChild(labelA)
stage.addChild(labelB)

stage.update()
Ticker.addEventListener("tick", stage)