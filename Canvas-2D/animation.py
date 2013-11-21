from browser import *
from workbench import *
from math import pi


useLargeCanvas = False

def backingScale(context):
    if window.devicePixelRatio and context.webkitBackingStorePixelRatio:
        return window.devicePixelRatio
    else:
        return 1

canvas = document.createElement("canvas")

workbench = Workbench2D(canvas)

context = canvas.getContext("2d")

pixelRatio = backingScale(context)
# Multiply width and height of canvas by the backing scale.
# Drawing instructions that refer to points in the coordinate space
# must also be multiplied by the backing scale.
canvas.height = 400 * pixelRatio
canvas.width = 400 * pixelRatio

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

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()