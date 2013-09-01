# Sep 1, 2013
# This is a work in progress. It may not work for you yet!
# The idea is to create a simple 3D visualization library.
# The library will be similar to Visual Python.
from e3ga import *
from vista import *
from browser import *
from math import pi

# Discard the old canvas if it exists. 
for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

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

mesh = Mesh(cube, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

requestID = None
progress = None
progressEnd = 10000
startTime =  None
movement = 0.02 * Vector3(1, 1, 1)

def render():
    mesh.rotation += movement
        
    renderer.render(scene, camera)

def onWindowResize(event):
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
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
        requestID = window.requestAnimationFrame(step)
        render()
    else:
        window.cancelAnimationFrame(requestID)
        # container.removeChild(renderer.domElement)

window.addEventListener("resize", onWindowResize, False)

onWindowResize(None)

animate(None)