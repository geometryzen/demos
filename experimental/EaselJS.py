from easel import *
from browser import *

def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
def handleComplete():
    print "The tween is complete"
        
discardCanvases()
canvas = document.createElement("canvas")
canvas.width = 960
canvas.height = 400
container = document.getElementById("canvas-container")
container.appendChild(canvas)

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