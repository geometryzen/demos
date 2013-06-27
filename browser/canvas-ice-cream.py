# Under Construction.
# HTML5 Canvas demonstration.
# We will control the horizontal. We will control the vertical.
from browser import *

# Convenince variable controlling whether we embed in the existing canvas container
# or create a nearly full screen canvas
useLargeCanvas = False
CANVAS_TAGNAME = "canvas"

# Variables to track the intentions of the user.
moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

# Global variables
print window.devicePixelRatio
view = document.getElementById("view")
canvas = document.createElement(CANVAS_TAGNAME)
canvas.style.position = "absolute"
canvas.style.top = "0px"
canvas.style.left = "0px"
canvas.width = 400
canvas.height = 400
#canvas.style.width = str(canvas.width) + "px"
#canvas.style.height = str(canvas.height) + "px"
#context = canvas.getContext("experimental-webgl")

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
        canvas.width = window.innerWidth
        canvas.height = window.innerHeight
        canvas.style.width = str(window.innerWidth) + "px"
        canvas.style.height = str(window.innerHeight) + "px"
    else:
        container = document.getElementById("canvas-container")
        canvas.width = container.clientWidth
        canvas.height = container.clientHeight
        canvas.style.width = str(container.clientWidth) + "px"
        canvas.style.height = str(container.clientHeight) + "px"
    
def discardExistingCanvas():
    for es in document.getElementsByTagName(CANVAS_TAGNAME):
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
    x = 1

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

print "ESC to terminate, Arrow keys to move Left, Right, Forward, Backward."
print "This program will self-destruct in 60 seconds."
init()
animate(None)
