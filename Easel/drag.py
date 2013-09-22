from easel import *
from browser import *

def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)

def onMouseDown(event):
    x = event.target.x - event.stageX
    y = event.target.y - event.stageY
    def onMouseMove(event):
        event.target.x = event.stageX + x
        event.target.y = event.stageY + y
        stage.update()
    event.addEventListener("mousemove", onMouseMove)

discardCanvases()

canvas = document.createElement("canvas")

stage = Stage(canvas)
stage.mouseMoveOutside = True

circle = Shape()
circle.graphics.beginFill("#000000").drawCircle(0, 0, 50).endFill()
circle.name = "circle"

label = Text("drag me", "bold 14px Arial", "#FFFFFF")
label.textAlign = "center"
label.y = -7

dragger = Container()
dragger.x = dragger.y = 100
dragger.addChild(circle)
dragger.addChild(label)
stage.addChild(dragger)

dragger.addEventListener("mousedown", onMouseDown)

stage.update()

workbench2D = Workbench2D(canvas)

def setUp():
    workbench2D.setUp()
    pass

def tick(t):
    pass

def terminate(t):
    return t > 6


def tearDown():
    workbench2D.tearDown()
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
