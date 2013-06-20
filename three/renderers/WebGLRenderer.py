# WebGLRenderer demonstration.
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
renderer.autoClear = False

print repr(renderer)
print "autoClear:         " + str(renderer.autoClear)
print str(renderer)
print renderer

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

radius = 50
widthSegments = 32
heightSegments = 24
phiStart = 0
phiLength = 2 * pi
thetaStart = 0
thetaLength = pi
sphere = SphereGeometry(radius, widthSegments, heightSegments, phiStart, phiLength, thetaStart, thetaLength)

mesh = Mesh(sphere, MeshNormalMaterial())
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
        # container.removeChild(renderer.domElement)
        # TODO: Remove the "resize" event listener

window.addEventListener("resize", onWindowResize, False)

onWindowResize()

step(None)