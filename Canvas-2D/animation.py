#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#        1         2         3         4         5         6         7         8
from browser import *
from workbench import *
from math import pi

canvas = document.createElement("canvas")

workbench = Workbench2D(canvas)

context = canvas.getContext("2d")

progressEnd = 3
        
step = 0
steps = 50
addAngle = 2 * pi / steps
addScale = 1.0 / steps

def setUp():
    workbench.setUp()

def tick(t):
    global step
    if step < steps:
        step += 1
    # Changing the canvas width or height resets the canvas.
    context.fillStyle = "blue"
    context.font = "24pt Helvetica"
    context.textAlign = "center"
    context.textBaseline = "middle"
    context.clearRect(0, 0, canvas.width, canvas.height)
    context.save()
    context.translate(canvas.width / 2, canvas.height / 2)
    context.scale(addScale * step, addScale * step)
    context.rotate(addAngle * step)
    context.fillText("Geometry Zen", 0, 0)
    context.restore()

def terminate(t):
    return t > progressEnd
    
def tearDown():
    workbench.tearDown()

war = WindowAnimationRunner(tick, terminate, setUp, tearDown)
war.start()
