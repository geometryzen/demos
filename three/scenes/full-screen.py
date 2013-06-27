# Demonstrates manipulating the document object model to make a canvas near full-screen.
from three import *
from browser import *

container = document.createElement("div")
document.body.appendChild(container)

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2

renderer = WebGLRenderer()

view = document.getElementById("view")
view.parentNode.insertBefore(renderer.domElement, view)

mesh = Mesh(CubeGeometry(1.0, 1.0, 1.0), MeshNormalMaterial())
scene.add(mesh)

requestID = None
progress = None
progressEnd = 6000
startTime =  None

def render():
    mesh.rotation.x = mesh.rotation.x + 0.02
    mesh.rotation.y = mesh.rotation.y + 0.02
    mesh.rotation.z = mesh.rotation.z + 0.02
        
    renderer.render(scene, camera)

def onWindowResize():
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)
    
def step(timestamp):
    global requestID, progress, startTime
    if (startTime):
        progress = timestamp - startTime
    else:
        if (timestamp):
            startTime = timestamp
        else:
            progress = 0
        
    if (progress < progressEnd):
        requestID = window.requestAnimationFrame(step)
        render()
    else:
        window.cancelAnimationFrame(requestID)
        view.parentNode.removeChild(renderer.domElement)

window.addEventListener("resize", onWindowResize, False)
onWindowResize()

step(None)
