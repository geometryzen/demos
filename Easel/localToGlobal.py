from easel import *
from browser import *
from workbench import *
from math import pi

canvas = document.createElement("canvas")

stage = Stage(canvas)

target = stage.addChild(Shape())
target.graphics.beginFill("blue").drawCircle(0, 0, 50).endFill()
target.graphics.beginFill("white").drawCircle(0, 0, 30).endFill()
target.graphics.beginFill("red").drawCircle(0, 0, 10).endFill()
target.x = 100
target.y = 180

arm = stage.addChild(Shape())
arm.graphics.beginFill("black").drawRect(-2, -2, 100, 4).endFill()
arm.graphics.beginFill("black").drawCircle(100, 0, 8).endFill()
arm.x = 180
arm.y = 100

workbench2D = Workbench2D(canvas)

def setUp():
    workbench2D.setUp()

def tick(t):
    arm.rotation = 180 * t
    target.alpha = 0.2
    point = arm.localToLocal(100, 0, target)
    if target.hitTest(point.x, point.y):
        target.alpha = 1
    stage.update()
    
def terminate(t):
    return t > 10

def tearDown(e):
    workbench2D.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()