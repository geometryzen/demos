# Under Construction
from browser import *

useLargeCanvas = False

canvas = document.createElement("canvas")
canvas.height = 400
canvas.width = 400

context = canvas.getContext("2d")

def escKey(downFlag):
    terminate()
    
keyHandlers = {
 27: escKey
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](True)
        event.preventDefault()
    except:
        print "X"
        
def onDocumentKeyUp(event):
    try:
        keyHandlers[event.keyCode](False)
        event.preventDefault()
    except:
        print "Y"


def onWindowResize():
    if (useLargeCanvas):
        canvas.width = window.innerWidth
        canvas.height = window.innerHeight
    else:
        container = document.getElementById("canvas-container")
        canvas.width = container.clientWidth
        canvas.height = container.clientHeight
    
def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
requestID = None
progress = None
progressEnd = 60000
startTime =  None

def init():
    print "Hello!"
    print "This program demonstrates the use of the Mouse."        
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
    context.strokeStyle = "#808080" 

    context.clearRect(-200, -200, 400, 400)
    context.font = "48pt Arial"
    context.strokeText("Hello, Mouse", 60, 60)
    
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
    print "Goodbye."

init()
animate(None)
