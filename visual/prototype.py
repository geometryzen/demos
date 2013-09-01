# Sep 1, 2013
# This is a work in progress. It may not work for you yet!
# The idea is to create a simple 3D visualization library.
# The library will be similar to Visual Python.
from eight import *
from browser import *

for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = world()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(2, 2, 2)
camera.lookAt(scene.position)

camera2 = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera2.position.set(-2, -2, -2)
camera2.lookAt(scene.position)

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 0.5)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

shape = cylinder()

scene.add(shape)

requestID = None
progress = None
progressEnd = 6000
startTime = None
movement = Vector3(0.02, 0.02, 0.02)

def render():
    shape.rotation += movement
        
    renderer.render(scene, camera)
    renderer.render(scene, camera2)

def onWindowResize(event):
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    camera2.aspect = window.innerWidth / window.innerHeight
    camera2.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)
    
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
        window.cancelAnimationFrame(requestID)
        # container.removeChild(renderer.domElement)

window.addEventListener("resize", onWindowResize, False)

onWindowResize(None)

animate(None)