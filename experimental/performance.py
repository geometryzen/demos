# performance.py
# particle.py
# Under Construction!
from eight import *
from browser import *

useLargeCanvas = False

moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

camera  = PerspectiveCamera(45, 1.0, 0.1, 1000)
camera.position.z = 20
renderer = WebGLRenderer({"antialias": True})
renderer.setClearColor(0xFFFFFF, 1.0)
scene = Scene()
particle = Mesh(SphereGeometry(1.0, 32, 24), MeshLambertMaterial({"color":0x0000FF}))
scene.add(particle)

ambientLight = AmbientLight(0x111111)
scene.add(ambientLight)

pointLight = PointLight(0xFFFFFF)
pointLight.position.set(20, 20, 20)
scene.add(pointLight)

directionalLight = DirectionalLight(0xFFFFFF)
directionalLight.position.set(0, 1, 0)
scene.add(directionalLight)

graph = document.createElement("canvas")
graph.style.position = "absolute"
graph.style.top = "0px"
graph.style.left = "0px"
context = graph.getContext("2d")

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
        graph.width = window.innerWidth
        graph.height = window.innerHeight
        graph.style.width = str(window.innerWidth) + "px"
        graph.style.height = str(window.innerHeight) + "px"
    else:
        container = document.getElementById("canvas-container")
        camera.aspect = container.clientWidth / container.clientHeight
        camera.updateProjectionMatrix()
        renderer.setSize(container.clientWidth, container.clientHeight)
        graph.width = container.clientWidth
        graph.height = container.clientHeight
        graph.style.width = str(container.clientWidth) + "px"
        graph.style.height = str(container.clientHeight) + "px"
    
def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
requestID = None
frameIndex = 0
DURATION_MILLISECONDS = 5000
startTime =  None
frameTime = None
endTime = None

particle.position = Vector3(-10,0,0)
velocity = Vector3(0.004,0,0)

def init():
    print "Hello!"
    print "This program is an exploration of ways to improve the user experience."        
    print "Press ESC to terminate."
    print "This program will 'self-terminate' in "+str(DURATION_MILLISECONDS/1000)+" seconds!"
    print "Try setting the useLargeCanvas variable to True. Then scroll down to see what is going on."
    discardCanvases()
    if (useLargeCanvas):
        document.body.insertBefore(renderer.domElement, document.body.firstChild)
        document.body.insertBefore(graph, document.body.firstChild)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(graph)
        container.appendChild(renderer.domElement)

    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()

def render(n, t, dt):
    n = n
#   particle.position = particle.position + velocity * dt
#    if moveForward:
#        camera.position.z -= 0.2
#    if moveBackward:
#        camera.position.z += 0.2
#    if moveLeft:
#        camera.position.x -= 0.2
#    if moveRight:
#        camera.position.x += 0.2
#    
#     particle.position = particle.position + velocity * dt
    
#    renderer.render(scene, camera)
    
def bootstrap(timestamp):
    global requestID, startTime, frameTime, endTime
    startTime = timestamp
    frameTime = timestamp
    endTime = startTime + DURATION_MILLISECONDS
    requestID = window.requestAnimationFrame(animate)
    render(frameIndex, frameTime, 0.0)
    
def animate(timestamp):
    global requestID, frameIndex, frameTime
    frameIndex += 1
    interval = timestamp - frameTime 
    frameTime = timestamp   
    if frameTime < endTime:
        requestID = window.requestAnimationFrame(animate)
        render(frameIndex, frameTime - startTime, interval)
    else:
        terminate()
        
def terminate():
    window.cancelAnimationFrame(requestID)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    time = (frameTime-startTime)/1000
    count = frameIndex+1
    print {'count':count,'time':time,'rate':count/time,'dt':time/frameIndex}
    print "Goodbye."

init()
window.requestAnimationFrame(bootstrap)
