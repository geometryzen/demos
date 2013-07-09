# Supporting High Resolution Displays
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
print "backingScale => " + str(pixelRatio)
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
    context.save()
    context.rotate(pi/4) # Not seeing this do much?
    context.setTransform(1, 0, 0, 1, 0, 0)
    context.fillStyle = "rgba(255, 102, 207, 1.0)" # "#FF66CC"
    context.strokeStyle = "#808080"
    context.lineWidth = 2 * pixelRatio

    context.clearRect(-200, -200, 400, 400)

    context.fillRect(0*pixelRatio, 0*pixelRatio, 50*pixelRatio, 50*pixelRatio)
    context.fillRect(100*pixelRatio, 100*pixelRatio, 50*pixelRatio, 50*pixelRatio)
    context.strokeRect(75*pixelRatio, 75*pixelRatio, 50*pixelRatio, 50*pixelRatio)

    context.beginPath()
    context.moveTo(0*pixelRatio,30*pixelRatio)
    context.lineTo(0*pixelRatio,100*pixelRatio)
    # center
    context.moveTo(-10, 0)
    context.lineTo(10, 0)
    context.moveTo(0, -10)
    context.lineTo(0, 10)
    context.fill()
    context.rect(0*pixelRatio,0*pixelRatio,100*pixelRatio,100*pixelRatio)
    context.rect(0*pixelRatio,0*pixelRatio,200*pixelRatio,200*pixelRatio)
    context.rect(0*pixelRatio,0*pixelRatio,300*pixelRatio,300*pixelRatio)
    context.rect(10*pixelRatio, 10*pixelRatio, 50*pixelRatio, 50*pixelRatio)

    context.strokeText("Hello, Canvas", 60, 60)

    context.closePath()
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
