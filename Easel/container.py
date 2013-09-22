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

circle = Shape()
circle.graphics.beginFill("red").drawCircle(0, 0, 50).endFill()
circle.name = "circle"

label = Text("click me!", "bold 14px Arial", "#FFFFFF")
label.textAlign = "center"
label.y = -7

button = Container()
button.name ="button"
button.x = button.y = 100
button.addChild(circle)
button.addChild(label)
stage.addChild(button)

def handleClick(event):
    print "Clicked on: " + str(event.target)

circle.addEventListener("click", handleClick)
label.addEventListener("click", handleClick)
button.addEventListener("click", handleClick)

stage.update()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
