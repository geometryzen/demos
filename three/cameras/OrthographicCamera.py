# OrthographicCamera.py
from three import *
from browser import *

useLargeCanvas = False

# Variables to track the intentions of the user.
moveForward = False
moveBackward = False
moveLeft = False
moveRight = False

# Global variables
camera  = OrthographicCamera(-1, 1, 1, -1, -500, 1000)
camera.position.x = 200
camera.position.y = 100
camera.position.z = 200
print repr(camera)
print str(camera)
renderer = WebGLRenderer({"antialias": True})
scene = Scene()
view = document.getElementById("view")
requestID = None
progress = None
progressEnd = 6000
startTime =  None

def onWindowResize():
    if (useLargeCanvas):
        halfW = window.innerWidth / 2
        halfH = window.innerHeight / 2
        
        camera.left   = -halfW
        camera.right  =  halfW
        camera.top    =  halfH
        camera.bottom = -halfH
        print repr(camera)
        camera.updateProjectionMatrix()
        renderer.setSize(window.innerWidth, window.innerHeight)
    else:
        container = document.getElementById("canvas-container")
        halfW = container.clientWidth / 2
        halfH = container.clientHeight / 2
        
        camera.left   = -halfW
        camera.right  =  halfW
        camera.top    =  halfH
        camera.bottom = -halfH
        print repr(camera)
        camera.updateProjectionMatrix()
        renderer.setSize(container.clientWidth, container.clientHeight)
    
def discardExistingCanvas():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)

def init():
    discardExistingCanvas()
    if (useLargeCanvas):
        container = document.createElement("div")
        document.body.appendChild(container)
        view.parentNode.insertBefore(renderer.domElement, view)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(renderer.domElement)

    # Grid
    size = 500
    step = 50
    geometry = Geometry()
    for i in range(-size, size+step, step):
        geometry.vertices.append(Vector3(-size, 0, i))
        geometry.vertices.append(Vector3(+size, 0, i))
        geometry.vertices.append(Vector3( i, 0, -size))
        geometry.vertices.append(Vector3( i, 0, +size))
        print i

    mesh = Mesh(CubeGeometry(100.0, 100.0, 100.0), MeshNormalMaterial())
    scene.add(mesh)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()

def render():
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
        view.parentNode.removeChild(graph)
    else:
        discardExistingCanvas()
    print "Goodbye!"

print "This example will end automatically in "+str(progressEnd/1000)+" seconds."
init()
animate(None)
