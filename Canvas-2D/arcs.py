from browser import *
from math import pi

useLargeCanvas = False

moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

def backingScale(context):
    if window.devicePixelRatio and context.webkitBackingStorePixelRatio:
        return window.devicePixelRatio
    else:
        return 1

canvas = document.createElement("canvas")

context = canvas.getContext("2d")

pixelRatio = backingScale(context)
# Multiply width and height of canvas by the backing scale.
# Drawing instructions that refer to points in the coordinate space
# must also be multiplied by the backing scale.
canvas.height = 400 * pixelRatio
canvas.width = 400 * pixelRatio

def escKey(downFlag):
    terminate()

def leftArrowKey(downFlag):
    global moveLeft
    moveLeft = downFlag

def upArrowKey(downFlag):
    global moveForward
    moveForward = downFlag
    
def rightArrowKey(downFlag):
    global moveRight
    moveRight = downFlag

def downArrowKey(downFlag):
    global moveBackward
    moveBackward = downFlag

keyHandlers = {
 27: escKey,
 37: leftArrowKey,
 38: upArrowKey,
 39: rightArrowKey,
 40: downArrowKey
}
    
def onDocumentKeyDown(event):
    event.preventDefault()
    keyHandlers[event.keyCode](True)

def onDocumentKeyUp(event):
    event.preventDefault()
    keyHandlers[event.keyCode](False)

def onWindowResize():
    if (useLargeCanvas):
        canvas.width = window.innerWidth * pixelRatio
        canvas.height = window.innerHeight * pixelRatio
    else:
        container = document.getElementById("canvas-container")
        canvas.width = container.clientWidth * pixelRatio
        canvas.height = container.clientHeight * pixelRatio
    
def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
requestID = None
progress = None
progressEnd = 60000
startTime =  None

def init():
    print "Press ESC to terminate."
    print "This program will 'self-terminate' in "+str(progressEnd/1000)+" seconds!"
    discardCanvases()
    if useLargeCanvas:
        document.body.insertBefore(canvas, document.body.firstChild)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(canvas)
    
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()

def render():
    context.strokeStyle = "black"
    context.arc(canvas.width/2,canvas.height/2,50,0,2*pi)
    context.stroke()

    
def animate(timestamp):
    global requestID, progress, startTime
    if startTime:
        progress = timestamp - startTime
    else:
        if timestamp:
            startTime = timestamp
        else:
            progress = 0
        
    if progress < progressEnd:
        requestID = window.requestAnimationFrame(animate)
        render()
    else:
        terminate()
        
def terminate():
    window.cancelAnimationFrame(requestID)
    discardCanvases()
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    print "Done."

init()
animate(None)
