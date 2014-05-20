# How to move the camera using the keyboard events.
from three import *
from browser import *
from workbench import *

moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2
renderer = WebGLRenderer({"antialias": True})
scene = Scene()

def escKey(downFlag):
    global timeOut
    timeOut = 0

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

timeOut = 10

workbench = Workbench3D(renderer.domElement, renderer, camera)

def setUp():
    print "Hello!"
    print "This program is a demonstration of the HTML5 WebGL Canvas."        
    print "Press ESC to terminate, Arrow keys to move the 3D cube Left, Right, Forward, Backward."
    print "This program will 'self-terminate' in "+str(timeOut)+" seconds!"
    workbench.setUp()

    mesh = Mesh(CubeGeometry(1.0, 1.0, 1.0), MeshNormalMaterial())
    scene.add(mesh)
    
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)

def tick(t):
    if moveForward:
        camera.position.z -= 0.02
    if moveBackward:
        camera.position.z += 0.02
    if moveLeft:
        camera.position.x -= 0.02
    if moveRight:
        camera.position.x += 0.02

    renderer.render(scene, camera)
    
def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    workbench.tearDown()
    print "Goodbye."

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
