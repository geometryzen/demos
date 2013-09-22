'''
Experiment to combine HTML5 2d and WebGL 3D graphics to support demos.
'''
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

graph = document.createElement("canvas")
graph.height = window.innerHeight
graph.width = window.innerWidth
graph.style.position = "absolute"
graph.style.top = "0px"
graph.style.left = "0px"

context = graph.getContext("2d")

def escKey(downFlag, event):
    event.preventDefault()
    global timeOut
    timeOut = 0

def leftArrowKey(downFlag, event):
    event.preventDefault()
    global moveLeft
    moveLeft = downFlag

def upArrowKey(downFlag, event):
    event.preventDefault()
    global moveForward
    moveForward = downFlag
    
def rightArrowKey(downFlag, event):
    event.preventDefault()
    global moveRight
    moveRight = downFlag

def downArrowKey(downFlag, event):
    event.preventDefault()
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
    try:
        keyHandlers[event.keyCode](True, event)
    except:
        pass

def onDocumentKeyUp(event):
    try:
        keyHandlers[event.keyCode](False, event)
    except:
        pass

# TODO: Resizing the HTML5 2d canvas
def onWindowResize():
    graph.width = window.innerWidth
    graph.height = window.innerHeight
        
timeOut = 10

workbench = Workbench(renderer, camera)

def setUp():
    print "Hello!"
    print "This program is a demonstration of mixing the HTML5 2d and WebGL 3D Canvases."        
    print "Press ESC to terminate, Arrow keys to move the 3D cube Left, Right, Forward, Backward."
    print "This program will 'self-terminate' in "+str(timeOut)+" seconds!"
    workbench.setUp()
    document.body.insertBefore(graph, document.body.firstChild)

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

    renderer.render(scene, camera)
    
def terminate(t):
    return t > timeOut
    
def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    workbench.tearDown()
    print "Goodbye."

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
