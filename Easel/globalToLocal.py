from easel import *
from browser import *
from random import random 

def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
discardCanvases()

canvas = document.createElement("canvas")
canvas.width = 300
canvas.height = 300
container = document.getElementById("canvas-container")
container.appendChild(canvas)

stage = Stage(canvas)

holder = stage.addChild(Container())
holder.x = holder.y = 150

for i in range(0, 25):
    shape = Shape()
    shape.graphics.beginFill(getHSL(random()*360,100,50)).drawCircle(0,0,30).endFill()
    shape.x = random() * 300 - 150
    shape.y = random() * 300 - 150
    holder.addChild(shape)

def tick():
    holder.rotation += 5
    n = holder.getNumChildren()
    for i in range(0, n):
        child = holder.getChildAt(i)
        child.alpha = 0.1
        pt = child.globalToLocal(stage.mouseX, stage.mouseY)
        if (stage.mouseInBounds and child.hitTest(pt.x, pt.y)):
            child.alpha = 1 
    stage.update()
    
Ticker.addEventListener("tick", tick)