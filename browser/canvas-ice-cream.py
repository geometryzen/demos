# HTML5 Canvas demonstration.
from browser import *
from math import pi

# Convenince variable controlling whether we embed in the existing canvas container
# or create a nearly full screen canvas
useLargeCanvas = False

# Variables to track the intentions of the user.
moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

# Global variables
view = document.getElementById("view")
canvas = document.createElement("canvas")
canvas.width = 400 * window.devicePixelRatio
canvas.height = 400 * window.devicePixelRatio
context = canvas.getContext("2d")

# Use Python's dictionary to handle event.keyCode(s).
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
    if (event.keyCode in keyHandlers):
        keyHandlers[event.keyCode](True)
        event.preventDefault()

def onDocumentKeyUp(event):
    if (event.keyCode in keyHandlers):
        keyHandlers[event.keyCode](False)
        event.preventDefault()

def onWindowResize():
    if (useLargeCanvas):
        canvas.width = window.innerWidth * window.devicePixelRatio
        canvas.height = window.innerHeight * window.devicePixelRatio
        canvas.style.width = str(window.innerWidth) + "px"
        canvas.style.height = str(window.innerHeight) + "px"
    else:
        container = document.getElementById("canvas-container")
        canvas.width = container.clientWidth * window.devicePixelRatio
        canvas.height = container.clientHeight * window.devicePixelRatio
        canvas.style.width = str(container.clientWidth) + "px"
        canvas.style.height = str(container.clientHeight) + "px"
    
def discardExistingCanvas():
    for es in document.getElementsByTagName("canvas"):
        es.parentNode.removeChild(es)
        
requestID = None
progress = None
progressEnd = 60000
startTime =  None

def init():
    discardExistingCanvas()
    if (useLargeCanvas):
        container = document.createElement("div")
        document.body.appendChild(container)
        view.parentNode.insertBefore(canvas, view)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(canvas)

    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()

def render():
    context.beginPath()
    context.moveTo(150, 100)
    context.lineTo(200, 225)
    context.lineTo(250, 100)
    context.fillStyle = "#D3BEA5"
    context.fill()
    context.stroke()

    context.beginPath()
    context.arc(200, 100, 50, 0, pi, True)
    context.fillStyle = "#FB6CF9"
    context.fill()

    context.closePath()
    context.stroke()

def animate(timestamp):
    global requestID, progress, startTime
    if (startTime):
        progress = timestamp - startTime
    else:
        if (timestamp):
            startTime = timestamp
        else:
            progress = 0
        
    if (progress < progressEnd):
        requestID = window.requestAnimationFrame(animate)
        render()
    else:
        terminate()
        
def terminate():
    window.cancelAnimationFrame(requestID)
    if (useLargeCanvas):
        view.parentNode.removeChild(canvas)
    else:
        discardExistingCanvas()
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    print "done!"

print "ESC to terminate"
print "This program will self-destruct in 60 seconds."
init()
animate(None)
