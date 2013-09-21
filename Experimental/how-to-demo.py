from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *

space = CartesianSpace()
        
canvas = document.createElement("canvas")
workbench2D = Workbench2D(canvas)
workbench3D = Workbench(space.renderer, space.camera)

def setUp():
    print "Hello"
    workbench2D.setUp()
    workbench3D.setUp()

    stage = Stage(canvas)
    stage.autoClear = True

    ball = Shape()
    ball.graphics.setStrokeStyle(5, "round", "round")
    ball.graphics.beginStroke("#000000")
    ball.graphics.beginFill("#FF0000").drawCircle(0,0,50).endFill()
    ball.graphics.endStroke()
    ball.graphics.setStrokeStyle(1, "round", "round")
    ball.graphics.beginStroke("#000000")
    ball.graphics.moveTo(0,0)
    ball.graphics.lineTo(0,50)
    ball.graphics.endStroke()
    ball.x = 200
    ball.y = 100

    stage.addChild(ball)
    Ticker.addEventListener("tick", stage)

def tick(t):
    pass

def terminate(t):
    return t > 6

def tearDown():
    print "Goodbye"
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
