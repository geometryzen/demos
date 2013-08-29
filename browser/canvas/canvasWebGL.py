from three import *
from browser import *

useLargeCanvas = False

moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2
renderer = WebGLRenderer({"antialias": True})
scene = Scene()

view = document.getElementById("view")

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
        camera.aspect = window.innerWidth / window.innerHeight
        camera.updateProjectionMatrix()
        renderer.size = (window.innerWidth, window.innerHeight)
    else:
        container = document.getElementById("canvas-container")
        camera.aspect = container.clientWidth / container.clientHeight
        camera.updateProjectionMatrix()
        renderer.setSize(container.clientWidth, container.clientHeight)
    
def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
requestID = None
progress = None
progressEnd = 60000
startTime =  None

def init():
    print "Hello!"
    print "This program is a demonstration of the HTML5 WebGL Canvas."        
    print "Press ESC to terminate, Arrow keys to move the 3D cube Left, Right, Forward, Backward."
    print "This program will 'self-terminate' in "+str(progressEnd/1000)+" seconds!"
    print "Try setting the useLargeCanvas variable to True. Then scroll down to see what is going on."
    discardCanvases()
    if useLargeCanvas:
        document.body.insertBefore(renderer.domElement, document.body.firstChild)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(renderer.domElement)

    mesh = Mesh(CubeGeometry(1.0, 1.0, 1.0), MeshNormalMaterial())
    scene.add(mesh)
    
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()

def render():
    if moveForward:
        camera.position.z -= 0.02
    if moveBackward:
        camera.position.z += 0.02
    if moveLeft:
        camera.position.x -= 0.02
    if moveRight:
        camera.position.x += 0.02

    renderer.render(scene, camera)
    
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
