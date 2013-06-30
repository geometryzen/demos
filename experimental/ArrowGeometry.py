# Under Construction
# ArrowGeometry demonstration.
from eight import *
from browser import *
from math import pi

for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

radiusCone = 20
radiusShaft = 10
length = 80
lengthShaft = 60
a = Vector3(0, 0, length)
b = Vector3(radiusCone, 0, lengthShaft)
c = Vector3(radiusShaft, 0, lengthShaft)
d = Vector3(radiusShaft, 0, 0)
e = Vector3(0, 0, 0)
#points = [a, b, c, d, e, a]
points = [a, b, c, a]
arrow = LatheGeometry(points)

print repr(arrow)
print arrow

mesh = Mesh(arrow, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

requestID = None
progress = None
progressEnd = 18000
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