# CylinderGeometry demonstration.
from eight import *
from browser import *
from math import pi

# Discard the old canvas if it exists. 
for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

renderer = WebGLRenderer({"antialias": True})
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

radiusTop = 20
radiusBottom = 20
height = 100
radiusSegments = 32
heightSegments = 1
openEnded = False
cylinder = CylinderGeometry(radiusTop, radiusBottom, height, radiusSegments, heightSegments, openEnded)

print repr(cylinder)
print "radiusTop:      " + str(cylinder.radiusTop)
print "radiusBottom:   " + str(cylinder.radiusBottom)
print "height:         " + str(cylinder.height)
print "radiusSegments: " + str(cylinder.radiusSegments)
print "heightSegments: " + str(cylinder.heightSegments)
print "openEnded:      " + str(cylinder.openEnded)
print cylinder

mesh = Mesh(cylinder, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

requestID = None
progress = None
progressEnd = 10000
startTime =  None
movement = Vector3(0.02, 0.02, 0.02)

def render():
    mesh.rotation.add(movement)
        
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

window.addEventListener("resize", onWindowResize, False)

onWindowResize()

step(None)