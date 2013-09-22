from easel import *
from browser import *

def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
def onComplete(args):
    print "The tween is complete"
    print args
    print "Not all the args come through. Could be a bug in the TweenJS library?"
        
discardCanvases()
canvas = document.createElement("canvas")
canvas.width = 960
canvas.height = 400
container = document.getElementById("canvas-container")
container.appendChild(canvas)

stage = Stage(canvas)

Ticker.addEventListener("tick", stage)

movieClip = MovieClip(None, 0, False, {"start": 0, "middle": 40})
stage.addChild(movieClip)

target = Shape(Graphics().beginFill("#999999").drawCircle(100, 100, 100))

timeline = movieClip.timeline

target.alpha = 0
timeline.addTween(Tween.get(target).to({"alpha": 1}, 100).onComplete(onComplete, [11,22,33]))

movieClip.gotoAndPlay("middle")