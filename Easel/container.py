from easel import *
from browser import *
from workbench import *

canvas = document.createElement("canvas")

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

workbench2D = Workbench2D(canvas)

def setUp():
    circle.addEventListener("click", handleClick)
    label.addEventListener("click", handleClick)
    button.addEventListener("click", handleClick)
    pass

def tick(t):
    stage.update()

def terminate(t):
    return t > 10

def tearDown():
    circle.removeEventListener("click", handleClick)
    label.removeEventListener("click", handleClick)
    button.removeEventListener("click", handleClick)
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
