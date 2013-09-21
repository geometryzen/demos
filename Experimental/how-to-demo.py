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
print space
print space.renderer
print canvas3D
workbench3D = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def setUp():
    print "Hello"
    workbench2D.setUp()
    workbench3D.setUp()

    stage = Stage(canvas2D)
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

    tween = Tween.get(ball, {"loop": False})
    tween.to({"x":ball.x,"y":canvas.height - 55, "rotation":-360}, 1500, Ease.bounceOut)
    tween.wait(1000)
    tween.to({"x":canvas.width - 55, "rotation":360}, 2500, Ease.bounceOut)
    tween.wait(1000)
    tween.to({"scaleX":2, "scaleY":2, "x":canvas.width-110, "y":canvas.height-110}, 2500, Ease.bounceOut)
    tween.wait(1000)
    tween.to({"scaleX":0.5, "scaleY":0.5, "x":30, "y":canvas.height-30, "rotation":-360}, 2500, Ease.bounceOut)

    stage.addChild(ball)
    Ticker.addEventListener("tick", stage)

def tick(t):
    space.render()

def terminate(t):
    return t > 6

def tearDown():
    print "Goodbye"
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
