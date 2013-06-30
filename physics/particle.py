# Single particle subject to a user-defined force.
# The particle motion is simulated by integrating the velocity and position.
# The initial configuration is specified with Cartesian coordinates.
# The integration calculation is coordinate-free and is done with multivectors.
#
# TODO: This demonstration contains a lot of boilerplate code that could be put in a library.
# TODO: A 2D animation may be more appropriate in some cases and provide better graphing.
# TODO: Move the camera so that the z-axis is up, x-axis towards us and y to the right.
from eight import *
from browser import *

useLargeCanvas = False

camera  = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.z = 1000
renderer = WebGLRenderer()
renderer.setClearColor(0xFFFFFF, 1.0)
scene = Scene()

particle = Mesh(SphereGeometry(50, 32, 24), MeshLambertMaterial({"color":0x0000FF}))
scene.add(particle)

ambientLight = AmbientLight(0x222222)
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

keyHandlers = {
 27: escKey
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
DURATION_SECONDS = 15
startTime =  None
frameTime = None
endTime = None

# Initialize the system configuration
particle.position = Vector3(-400,0,0)
v = Vector3(75,75,0)
m = 1
g = Vector3(0, -9.81, 0)
E = Vector3()
B = Bivector3(0,0,0)
i = Vector3(1,0,0)
j = Vector3(0,1,0)
k = Vector3(0,0,1)
I = Pseudoscalar3(1)

def F(x,v,t):
    return m * g

def init():       
    print "Press ESC to terminate."
    print "This program will 'self-terminate' in "+str(DURATION_SECONDS)+" seconds!"
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
    global v
    # TODO: Implement Multivector division by at least scalars and vectors.    
    a = F(particle.position, v, t) * (1/m)
    v = v + a * dt
    particle.position = particle.position + v * dt
    
    renderer.render(scene, camera)

def bootstrap(timestamp):
    global requestID, startTime, frameTime, endTime
    startTime = timestamp
    frameTime = startTime
    endTime = startTime + DURATION_SECONDS * 1000
    requestID = window.requestAnimationFrame(animate)
    render(frameIndex, (frameTime - startTime)/1000, 0.0)
    
def animate(timestamp):
    global requestID, frameIndex, frameTime
    frameIndex += 1
    interval = timestamp - frameTime 
    frameTime = timestamp   
    if frameTime < endTime:
        requestID = window.requestAnimationFrame(animate)
        render(frameIndex, (frameTime - startTime)/1000, interval/1000)
    else:
        terminate()
        
def terminate():
    window.cancelAnimationFrame(requestID)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    time = (frameTime-startTime)/1000
    count = frameIndex+1
    print "Done."
    print "r: " + repr(particle.position)

init()
window.requestAnimationFrame(bootstrap)
