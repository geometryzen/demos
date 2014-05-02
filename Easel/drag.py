from easel import *
from browser import *
from workbench import *

def onMouseDown(event):
    x = event.target.x - event.stageX
    y = event.target.y - event.stageY
    def onMouseMove(event):
        event.target.x = event.stageX + x
        event.target.y = event.stageY + y
        stage.update()
    event.addEventListener("mousemove", onMouseMove)

canvas = document.createElement("canvas")

stage = Stage(canvas)
stage.mouseMoveOutside = True
dragger = Container()

workbench2D = Workbench2D(canvas)

def setUp():
    workbench2D.setUp()
    circle = Shape()
    circle.graphics.beginFill("#000000").drawCircle(0, 0, 50).endFill()
    circle.name = "circle"

    label = Text("drag me", "bold 14px Arial", "#FFFFFF")
    label.textAlign = "center"
    label.y = -7

    dragger.x = dragger.y = 100
    dragger.addChild(circle)
    dragger.addChild(label)
    stage.addChild(dragger)
    dragger.addEventListener("mousedown", onMouseDown)

def tick(t):
    stage.update()

def terminate(t):
    return t > 6

def tearDown(e):
    dragger.removeEventListener("mousedown", onMouseDown)
    workbench2D.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
