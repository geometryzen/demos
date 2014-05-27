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
    window.alert("Clicked on: " + str(event.target))

workbench = Workbench2D(canvas)

def setUp():
    workbench.setUp()
    circle.addEventListener("click", handleClick)
    label.addEventListener("click", handleClick)
    button.addEventListener("click", handleClick)

def tick(t):
    stage.update()

def terminate(t):
    return t > 10

def tearDown(e):
    circle.removeEventListener("click", handleClick)
    label.removeEventListener("click", handleClick)
    button.removeEventListener("click", handleClick)
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
