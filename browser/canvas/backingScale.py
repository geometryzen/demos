# Supporting High Resolution Displays
from browser import *

useLargeCanvas = False

moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

def backingScale(context):
    if window.devicePixelRatio and context.webkitBackingStorePixelRatio:
        return window.devicePixelRation
    else:
        return 1

graph = document.createElement("canvas")
graph.height = 400
graph.width = 400

context = graph.getContext("2d")

scale = backingScale(context)
print "backingScale => " + str(scale)

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
        graph.width = window.innerWidth
        graph.height = window.innerHeight
    else:
        container = document.getElementById("canvas-container")
        graph.width = container.clientWidth
        graph.height = container.clientHeight
    
def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
requestID = None
progress = None
progressEnd = 60000
startTime =  None

def init():
    print "Hello!"
    print "This program demonstrates the use of the HTML5 Canvas and the '2d' context."        
    print "Press ESC to terminate."
    print "This program will 'self-terminate' in "+str(progressEnd/1000)+" seconds!"
    print "Try setting the useLargeCanvas variable to True. Then scroll down to see what is going on."
    discardCanvases()
    if useLargeCanvas:
        document.body.insertBefore(graph, document.body.firstChild)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(graph)
    
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()

def render():
    context.setTransform(1, 0, 0, 1, 0, 0)
    context.fillStyle = "#FF66CC"
    context.strokeStyle = "#808080" 

    context.clearRect(-200, -200, 400, 400)

    context.fillRect(0, 0, 50, 50)
    context.fillRect(100, 100, 50, 50)
    context.strokeRect(75, 75, 50, 50)

    context.beginPath()
    context.moveTo(0,30)
    context.lineTo(0,100)
    # center
    context.moveTo(-10, 0)
    context.lineTo(10, 0)
    context.moveTo(0, -10)
    context.lineTo(0, 10)
    context.fill()
    context.rect(0,0,100,100)
    context.rect(0,0,200,200)
    context.rect(0,0,300,300)
    context.rect(10, 10, 50, 50)

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
    print "Goodbye."

init()
animate(None)
