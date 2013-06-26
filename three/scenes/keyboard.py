# Under Construction.
# Demonstrates keyboard handling.
from three import *
# We will control the horizontal. We will control the vertical.
from browser import *

moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

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

container = document.createElement("div")
document.body.appendChild(container)

scene = Scene()

# Aspect ratio will be reset in onWindowResize
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2

renderer = WebGLRenderer()

view = document.getElementById("view")
view.parentNode.insertBefore(renderer.domElement, view)

mesh = Mesh(CubeGeometry(1.0, 1.0, 1.0), MeshNormalMaterial())
scene.add(mesh)

requestID = None
progress = None
progressEnd = 10000 # run for 10 seconds
startTime =  None

def render():
    if (moveForward):
        camera.position.z -= 0.01
    if (moveBackward):
        camera.position.z += 0.01
    if (moveLeft):
        camera.position.x -= 0.01
    if (moveRight):
        camera.position.x += 0.01
        
    renderer.render(scene, camera)

def onWindowResize():
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)
    
    
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
    view.parentNode.removeChild(renderer.domElement)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    

document.addEventListener("keydown", onDocumentKeyDown, False)
document.addEventListener("keyup", onDocumentKeyUp, False)

window.addEventListener("resize", onWindowResize, False)
onWindowResize()

animate(None)
