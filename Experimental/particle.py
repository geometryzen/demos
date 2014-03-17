# Single particle subject to a user-defined force field.
# The particle motion is simulated by integrating the velocity and position.
# The initial configuration is specified with Cartesian coordinates.
# The integration calculation is coordinate-free and is done with multivectors.
#
# TODO: This demonstration contains a lot of boilerplate code that could be put in a library.
# TODO: A 2D animation may be more appropriate in some cases and provide better graphing.
# TODO: Move the camera so that the z-axis is up, x-axis towards us and y to the right.
from three import *
from browser import *

# TODO: This could be a particular coordinate system, not just a graphics scene?
scene = Scene()

particle = Mesh(SphereGeometry(50.0, 32, 24), MeshLambertMaterial({"color":0x0000FF}))
scene.add(particle)

# Initialize the system configuration.
x = VectorE3(-500.0, 0.0, 0.0)
v = VectorE3(75.0, 75.0, 0.0)
m = 1
g = VectorE3(0.0, -9.81, 0.0)

# Charge, Electric Field, and Magnetic Field as an bivector (no "dishonest" axial vectors, Thank You).
e = ScalarE3(1.0)
E = VectorE3(0.0, 0.0, 0.0)
B = BivectorE3(0.0, 0.0, 0.0)

# Some more examples of constructing reference multivectors.
one = Euclidean3(1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
i = VectorE3(1.0, 0.0, 0.0)
j = VectorE3(0.0, 1.0, 0.0)
k = VectorE3(0.0, 0.0, 1.0)
ij = i ^ j
jk = Euclidean3(0, 0, 0, 0, 0, 1, 0, 0)
ki = BivectorE3(0, 0, 1)
I = PseudoscalarE3(1)

# The user-defined force field, F, may depend upon the particle position, velocity and time.
def F(x,v,t):
    return m * g
    # TODO: Something like this for Electrodynamics (with vectors and bivectors).
    # No "dishonest" vectors here; Feynman would be proud!
    # return e * (E + (v << B))
    
def integrate(n, t, dt):
    global x, v

    a = F(x, v, t)/m
    v += a * dt
    x += v * dt
    # TODO: Implement a bounce with the Geometric reflection formula (-nvn).
    # TODO: Should we have Rigid Bodies with state/kinematic variables?
    # TODO: What about intrinsic properties such as mass or inertia tensor?
    particle.position.set(x.x, x.y, x.z)

useLargeCanvas = False

camera  = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.z = 1000
renderer = WebGLRenderer()
renderer.setClearColor(0xFFFFFF, 1.0)

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
    print "Done."
    print "x: " + str(x)
    print "v: " + repr(v)
    # TODO: It would be nice if standard mathematical function could be used on multivectors.
    print "v * v: " + repr(v * v)

run()
