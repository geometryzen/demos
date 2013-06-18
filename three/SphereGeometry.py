# SphereGeometry.py
from three import *
# We will control the horizontal. We will control the vertical.
from browser import *
from math import pi

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

# SphereGeometry(...)
# The arguments and their default values, in order, are...
radius = 50 # The radius of the sphere
widthSegments = 8 # The number of segments in the phi coordinate (min 3)
heightSegments = 6 # The number of segments in the theta coordinate (min 2)
phiStart = 0.5 * pi
phiLength = 2 * pi
thetaStart = 0
thetaLength = pi
# All arguments are optional.
geometry = SphereGeometry(radius, widthSegments, heightSegments, phiStart, phiLength, thetaStart, thetaLength)

print str(geometry)
print repr(geometry)

mesh = Mesh(geometry, MeshNormalMaterial())
scene.add(mesh)

requestID = None
progress = None
progressEnd = 2000
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