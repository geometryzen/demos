from easel import *
from browser import *
from workbench import *

def handleClick(event):
    window.alert("click => " + str(event))
        
canvas = document.createElement("canvas")

stage = Stage(canvas)
circle = stage.addChild(Shape())
circle.graphics.beginFill("red").drawCircle(0, 0, 50).endFill()
circle.x = 100
circle.y = 100

workbench2D = Workbench2D(canvas)

def setUp():
    workbench2D.setUp()
    circle.addEventListener("click", handleClick)

def tick(t):
    stage.update()

def terminate(t):
    return t > 5

def tearDown():
    circle.removeEventListener("click", handleClick)
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()