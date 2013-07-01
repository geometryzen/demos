# Under Construction
# Mesh demonstration.
from eight import *
from browser import *
from math import pi

i = Vector3(1,0,0)
j = Vector3(0,1,0)
k = Vector3(0,0,1)

for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

camera  = PerspectiveCamera(45, 1.0, 0.1, 1000)
camera.up.set(0,0,1)
camera.position.set(2,2,2)
camera.lookAt(scene.position)

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

length = 1
radiusShaft = length * 0.01
radiusCone = length * 0.1
lengthCone = length * 0.2
lengthShaft = length - lengthCone
a = Vector3(0, 0, length)
b = Vector3(radiusCone, 0, lengthShaft)
c = Vector3(radiusShaft, 0, lengthShaft)
d = Vector3(radiusShaft, 0, 0)
e = Vector3(0, 0, 0)
points = [a, b, c, d, e]

redWire = MeshLambertMaterial({"color":0xFF0000,"opacity":0.5,"transparent":True})
grnWire = MeshLambertMaterial({"color":0x00FF00,"opacity":0.5,"transparent":True})
bluWire = MeshBasicMaterial({"color":0x0000FF,"opacity":0.5,"transparent":True})
segments = 24

redGeom = LatheGeometry(points, segments)
grnGeom = LatheGeometry(points, segments)
bluGeom = LatheGeometry(points, segments)

redMesh = Mesh(redGeom, redWire)
redMesh.position.set(0,1,0)
redMesh.rotation.set(0,pi/2,0)
grnMesh = Mesh(bluGeom, grnWire)
grnMesh.rotation.set(-pi/2,0,0)
bluMesh = Mesh(grnGeom, bluWire)

scene.add(redMesh)
scene.add(bluMesh)
scene.add(grnMesh)

#ambientLight = AmbientLight(0x111111)
#scene.add(ambientLight)

pointLight = PointLight(0x888888)
pointLight.position.set(20, 20, 20)
scene.add(pointLight)

directionalLight = DirectionalLight(0x888888)
directionalLight.position.set(0, 1, 0)
scene.add(directionalLight)

requestID = None
progress = None
progressEnd = 6000
startTime =  None

def render():
        
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

window.addEventListener("resize", onWindowResize, False)

onWindowResize()

step(None)