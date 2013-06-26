# Under Construction.
# browser/canvas.py
from three import *
# We will control the horizontal. We will control the vertical.
from browser import *

# Convenince variable controlling whether we embed in the existing canvas container
# or create a nearly full screen canvas
useLargeCanvas = True

# Variables to track the intentions of the user.
moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

# Global variables
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
renderer = WebGLRenderer({"antialias": True})
scene = Scene()
view = document.getElementById("view")
debugCanvas = document.createElement("canvas")
debugCanvas.width = 512
debugCanvas.height = 512
debugCanvas.style.position = "absolute"
debugCanvas.style.top = "0px"
debugCanvas.style.left = "0px"
debugContext = debugCanvas.getContext("2d")
debugContext.setTransform(1, 0, 0, 1, 256, 256)
debugContext.strokeStyle = "#808080"

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
    event.preventDefault()
    keyHandlers[event.keyCode](True)

def onDocumentKeyUp(event):
    event.preventDefault()
    keyHandlers[event.keyCode](False)

def onWindowResize():
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)
    debugCanvas.width = window.innerWidth
    debugCanvas.height = window.innerHeight
    
def discardExistingCanvas():
    for canvas in document.getElementsByTagName("canvas"):
        canvas.parentNode.removeChild(canvas)
        
requestID = None
progress = None
progressEnd = 60000
startTime =  None

def init():
    discardExistingCanvas()
    if (useLargeCanvas):
        container = document.createElement("div")
        document.body.appendChild(container)
        view.parentNode.insertBefore(renderer.domElement, view)
        view.parentNode.insertBefore(debugCanvas, view)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(renderer.domElement)
        container.appendChild(debugCanvas)

    camera.position.z = 2

#    mesh = Mesh(CubeGeometry(1.0, 1.0, 1.0), MeshNormalMaterial())
#    scene.add(mesh)
    
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()

def render():
    if (moveForward):
        camera.position.z -= 0.02
    if (moveBackward):
        camera.position.z += 0.02
    if (moveLeft):
        camera.position.x -= 0.02
    if (moveRight):
        camera.position.x += 0.02
        
    debugContext.clearRect(-256, -256, 512, 512)
    debugContext.beginPath()
    
    # center
    debugContext.moveTo(-10, 0)
    debugContext.lineTo(10, 0)
    debugContext.moveTo(0, -10)
    debugContext.lineTo(0, 10)

    debugContext.rect(-50, -50, 100, 100)

    debugContext.closePath()
    debugContext.stroke()
      
    renderer.render(scene, camera)
    
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
        view.parentNode.removeChild(renderer.domElement)
        view.parentNode.removeChild(debugCanvas)
    else:
        discardExistingCanvas()
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)

print "ESC to terminate, Arrow keys to move Left, Right, Forward, Backward."
print "This program will self-destruct in 60 seconds."
init()
animate(None)
