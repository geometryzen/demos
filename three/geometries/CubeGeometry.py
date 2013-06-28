# CubeGeometry demonstration.
from eight import *
from browser import *
from math import pi

# Discard the old canvas if it exists. 
for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

# Aspect ratio will be reset in onWindowResize
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 20

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

width = 10
height = 10
depth = 10
widthSegments = 1
heightSegments = 1
depthSegments = 1
cube = CubeGeometry(width, height, depth, widthSegments, heightSegments, depthSegments)

print repr(cube)
print "width:          " + str(cube.width)
print "height:         " + str(cube.height)
print "depth:          " + str(cube.depth)
print "widthSegments:  " + str(cube.widthSegments)
print "heightSegments: " + str(cube.heightSegments)
print "depthSegments:  " + str(cube.depthSegments)
print cube

mesh = Mesh(cube, MeshNormalMaterial())
scene.add(mesh)

requestID = None
progress = None
progressEnd = 6000
startTime =  None
movement = 0.02 * Vector3(1, 1, 1)
print movement

def render():
    mesh.rotation.x = mesh.rotation.x + movement.x
    mesh.rotation.y = mesh.rotation.y + movement.y
    mesh.rotation.z = mesh.rotation.z + movement.z
        
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