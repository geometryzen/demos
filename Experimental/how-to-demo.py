from easel import *
from three import *
from browser import *
'''
Demonstrates combining the 2D Easel API and 3D Three Graphics API for building demonstrations.
This is probably going to be the most effective way to build interactive demonstrations.
'''
from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *

space = CartesianSpace()
        
canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)

canvas3D = space.renderer.domElement
workbench3D = Workbench3D(space.renderer.domElement, space.renderer, space.camera)
stage = Stage(canvas2D)
stage.autoClear = True

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()

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

    tween = Tween.get(ball, {"loop": False})
    tween.to({"x":ball.x,"y":canvas2D.height - 55, "rotation":-360}, 1500, Ease.bounceOut)
    tween.wait(1000)
    tween.to({"x":canvas2D.width - 55, "rotation":360}, 2500, Ease.bounceOut)
    tween.wait(1000)
    tween.to({"scaleX":2, "scaleY":2, "x":canvas2D.width-110, "y":canvas2D.height-110}, 2500, Ease.bounceOut)
    tween.wait(1000)
    tween.to({"scaleX":0.5, "scaleY":0.5, "x":30, "y":canvas2D.height-30, "rotation":-360}, 2500, Ease.bounceOut)

    stage.addChild(ball)
#   Ticker.addEventListener("tick", stage)

def tick(t):
    space.render()
    stage.update()

def terminate(t):
    return t > 15

def tearDown():
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
