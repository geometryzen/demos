from three import *
from browser import *
from math import pi

useLargeCanvas = False
COLOR_GRID = 0x66A1D2

scene = Scene()

particle = Mesh(SphereGeometry(float(50), 32, 24), MeshLambertMaterial({"color":0x0000FF}))
scene.add(particle)

xyPlane = Mesh(PlaneGeometry(1000.0,1000.0,10,10), MeshBasicMaterial({"color":COLOR_GRID, "wireframe":True, "opacity":0.2,"transparent":True}))
scene.add(xyPlane)
xyPlane.position.set(500,500,0)

yzPlane = Mesh(PlaneGeometry(1000.0,1000.0,10,10), MeshBasicMaterial({"color":COLOR_GRID, "wireframe":True, "opacity":0.2,"transparent":True}))
yzPlane.rotation.set(0,pi/2,0)
yzPlane.position.set(0,500,500)
scene.add(yzPlane)

zxPlane = Mesh(PlaneGeometry(1000.0,1000.0,10,10), MeshBasicMaterial({"color":COLOR_GRID, "wireframe":True, "opacity":0.2,"transparent":True}))
zxPlane.rotation.set(pi/2,0,0)
zxPlane.position.set(500, 0, 500)
scene.add(zxPlane)

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.up.set(0,0,1)
camera.position.set(1500,1500,1500)
camera.lookAt(scene.position)

# Initialize the system configuration.
x = VectorE3(0, 0, 0)
v = VectorE3(0,75,75)
m = 1
g = VectorE3(0, 0, -9.81)

# The user-defined force field, F, may depend upon the particle position, velocity and time.
def F(x,v,t):
    return m * g
    
def integrate(n, t, dt):
    global x, v

    a = F(x, v, t) / m
    v += a * dt
    x += v * dt
    particle.position.set(x.x, x.y, x.z)

renderer = WebGLRenderer()
renderer.setClearColor(0x080808, 1.0)

ambientLight = AmbientLight(0x222222)
scene.add(ambientLight)

pointLight = PointLight(0xFFFFFF)
pointLight.position.set(20, 20, 20)
scene.add(pointLight)

directionalLight = DirectionalLight(0xFFFFFF)
directionalLight.position.set(0, 1, 0)
scene.add(directionalLight)

# We're not actually using the HTML Canvas (2d), but it is here just in case we need it.
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

def run():       
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
    window.requestAnimationFrame(frameZero)

def frameZero(timestamp):
    global requestID, startTime, frameTime, endTime
    startTime = timestamp
    frameTime = startTime
    endTime = startTime + DURATION_SECONDS * 1000
    requestID = window.requestAnimationFrame(animate)
    integrate(frameIndex, (frameTime - startTime)/1000, 0.0)
    renderer.render(scene, camera)
    
def animate(timestamp):
    global requestID, frameIndex, frameTime
    frameIndex += 1
    interval = timestamp - frameTime 
    frameTime = timestamp   
    if frameTime < endTime:
        requestID = window.requestAnimationFrame(animate)
        integrate(frameIndex, (frameTime - startTime)/1000, interval/1000)
        renderer.render(scene, camera)
    else:
        terminate()
        
def terminate():
    window.cancelAnimationFrame(requestID)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    time = (frameTime-startTime)/1000
    count = frameIndex+1
    if useLargeCanvas:
        discardCanvases()
    print "Done."

run()
