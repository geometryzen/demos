from easel import *
from browser import *

def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
discardCanvases()
canvas = document.createElement("canvas")
canvas.width = 960
canvas.height = 400
container = document.getElementById("canvas-container")
container.appendChild(canvas)

stage = Stage(canvas)

Ticker.addEventListener("tick", stage)

movieClip = MovieClip(None, 0, True, {"start": 0, "middle": 40})
stage.addChild(movieClip)

child1 = Shape(Graphics().beginFill("#999999").drawCircle(100, 100, 100))
child2 = Shape(Graphics().beginFill("#5a9cfb").drawCircle(100, 100, 100))

timeline = movieClip.timeline

timeline.addTween(Tween.get(child1).to({"x": 0}).to({"x":760}, 40).to({"x": 0}, 40))
timeline.addTween(Tween.get(child2).to({"x": 760}).to({"x":0}, 40).to({"x": 760}, 40))

movieClip.gotoAndPlay("middle")