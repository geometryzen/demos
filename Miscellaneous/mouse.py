# Under Construction
from browser import *

useLargeCanvas = False

canvas = document.createElement("canvas")
canvas.height = 400
canvas.width = 400

context = canvas.getContext("2d")

screenX = 0
screenY = 0
clientX = 0
clientY = 0
button = 0
    
def onDocumentKeyDown(event):
    if event.keyCode == 27:
        terminate()

def onDocumentMouseDown(event):
    global screenX, screenY, clientX, clientY
    screenX = event.screenX
    screenY = event.screenY
    clientX = event.clientX
    clientY = event.clientY
    button = event.button
    if event.altKey:
        print "ALT"
    if event.ctrlKey:
        print "CTRL"
    if event.shiftKey:
        print "SHIFT"
    event.stopPropagation()
    event.stopImmediatePropagation()
    print {"cancelable": event.cancelable}
    print event.bubbles
    print event.defaultPrevented

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
    
    document.addEventListener('keydown', onDocumentKeyDown, False)
    document.addEventListener('mousedown', onDocumentMouseDown, False)

    window.addEventListener('resize', onWindowResize, False)
    onWindowResize()

def render():
    context.strokeStyle = "#808080" 
    
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
    window.removeEventListener('resize', onWindowResize, False)
    document.removeEventListener('keydown', onDocumentKeyDown, False)
    document.removeEventListener('mousedown', onDocumentMouseDown, False)
    print "Goodbye."

init()
animate(None)
