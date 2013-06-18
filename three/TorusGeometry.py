# TorusGeometry
from three import *
# We will control the horizontal. We will control the vertical.
from browser import *

# Discard the old canvas if it exists. 
for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

# Aspect ratio will be reset in onWindowResize
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

renderer = WebGLRenderer()

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

# TorusGeometry(radius, tube, radialSegments, tubularSegments, arc)
#
# @param radius=100
# @param tube=40
# @param radialSegments=8
# @param tubularSegments=6
# @param arc=Math.PI * 2
geometry = TorusGeometry(100, 40, 8, 6, 3.14159 * 2)
mesh = Mesh(geometry, MeshNormalMaterial())
scene.add(mesh)

requestID = None
progress = None
progressEnd = 10000 # run for 10 seconds
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
        # container.removeChild(renderer.domElement)
        # TODO: Remove the "resize" event listener

window.addEventListener("resize", onWindowResize, False)

onWindowResize()

step(None)