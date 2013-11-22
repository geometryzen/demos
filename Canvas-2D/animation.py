from browser import *
from workbench import *
from math import pi

canvas = document.createElement("canvas")

workbench = Workbench2D(canvas)

context = canvas.getContext("2d")

progressEnd = 3

def escKey(downFlag):
    global progressEnd
    progressEnd = 0

keyHandlers = {
 27: escKey
}
    
def onDocumentKeyDown(event):
    event.preventDefault()
    keyHandlers[event.keyCode](True)

def onDocumentKeyUp(event):
    event.preventDefault()
    keyHandlers[event.keyCode](False)

        
step = 0
steps = 50
addAngle = 2 * pi / steps
addScale = 1.0 / steps

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)

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
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    workbench.tearDown()

war = WindowAnimationRunner(tick, terminate, setUp, tearDown)
war.start()
