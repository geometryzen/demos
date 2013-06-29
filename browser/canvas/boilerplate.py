# This program is an on-going experiment to improve the experience for Computational Modeling students.
# Geometry Zen is very flexible, but does not yet provide ease-of-use features or modules to improve
# the experience for exploration and demonstration.
# The 'eight' module provides the 3D graphics API and Geometric Algebra in Euclidean 3D-space.
from eight import *
# The 'browser' module provides an API to the window and document as well as the HTML5 2D canvas.
from browser import *
# Change this variable render the graphics in different ways. 
useLargeCanvas = False
useWebGL = True

# Variables to track the intentions of the user.
moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

if useWebGL:
    camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
    camera.position.z = 2
    renderer = WebGLRenderer({"antialias": True})
    scene = Scene()
view = document.getElementById("view")
graph = document.createElement("canvas")
# Initialize the graph extent before we get resized to the container.
graph.height = 400
graph.width = 400
# Use absolute positioning so that the WebGL and Printer aren't pushed down.
graph.style.position = "absolute"
graph.style.top = "0px"
graph.style.left = "0px"

context = graph.getContext("2d")

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
    if (useLargeCanvas):
        if useWebGL:
            camera.aspect = window.innerWidth / window.innerHeight
            camera.updateProjectionMatrix()
            renderer.size = (window.innerWidth, window.innerHeight)
        graph.width = window.innerWidth
        graph.height = window.innerHeight
    else:
        container = document.getElementById("canvas-container")
        if useWebGL:
            camera.aspect = container.clientWidth / container.clientHeight
            camera.updateProjectionMatrix()
            renderer.setSize(container.clientWidth, container.clientHeight)
        graph.width = container.clientWidth
        graph.height = container.clientHeight
    
def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
requestID = None
progress = None
progressEnd = 600000
startTime =  None

def init():
    print "Hello!"
    print "This program is an exploration of ways to improve the user experience."        
    print "Press ESC to terminate, Arrow keys to move the 3D cube Left, Right, Forward, Backward."
    print "This program will 'self-terminate' in "+str(progressEnd/1000)+" seconds!"
    print "Try setting the useLargeCanvas variable to True. Then scroll down to see what is going on."
    discardCanvases()
    if useLargeCanvas:
        container = document.createElement("div")
        document.body.appendChild(container)
        if useWebGL:
            view.parentNode.insertBefore(renderer.domElement, view)
        view.parentNode.insertBefore(graph, view)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(graph)
        if useWebGL:
            container.appendChild(renderer.domElement)

    if useWebGL:
        mesh = Mesh(CubeGeometry(1.0, 1.0, 1.0), MeshNormalMaterial())
        scene.add(mesh)
    
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()

def render():
    if moveForward and useWebGL:
        camera.position.z -= 0.02
    if moveBackward and useWebGL:
        camera.position.z += 0.02
    if moveLeft and useWebGL:
        camera.position.x -= 0.02
    if moveRight and useWebGL:
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
    if useWebGL:
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
