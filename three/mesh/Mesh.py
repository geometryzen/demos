# Mesh demonstration.
from three import *
from browser import *
from math import pi

for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

camera  = PerspectiveCamera(45, 1.0, 0.1, 1000)
camera.position.z = 3

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

length = 1
radiusShaft = length * 0.05
radiusCone = radiusShaft * 2
lengthCone = radiusCone * 2
lengthShaft = length - lengthCone
a = Vector3(0, 0, length)
b = Vector3(radiusCone, 0, lengthShaft)
c = Vector3(radiusShaft, 0, lengthShaft)
d = Vector3(radiusShaft, 0, 0)
e = Vector3(0, 0, 0)
points = [a, b, c, d, e]

redWire = MeshBasicMaterial({"color":0xFF0000, "wireframe":True, "wireframeLinewidth":3})
bluWire = MeshBasicMaterial({"color":0x0000FF, "wireframe":True, "wireframeLinewidth":3})
grnWire = MeshBasicMaterial({"color":0x00FF00, "wireframe":True, "wireframeLinewidth":3})
yloWire = MeshBasicMaterial({"color":0xFFFF00, "wireframe":True, "wireframeLinewidth":3})
segments = 3

redGeom = LatheGeometry(points, segments)
grnGeom = LatheGeometry(points, segments)
bluGeom = LatheGeometry(points, segments)

redMesh = Mesh(redGeom, redWire)
bluMesh = Mesh(grnGeom, bluWire)
grnMesh = Mesh(bluGeom, grnWire)

scene.add(redMesh)
scene.add(bluMesh)
scene.add(grnMesh)

ambientLight = AmbientLight(0x222222)
scene.add(ambientLight)

pointLight = PointLight(0xFFFFFF)
pointLight.position.set(20, 20, 20)
scene.add(pointLight)

directionalLight = DirectionalLight(0xFFFFFF)
directionalLight.position.set(0, 1, 0)
scene.add(directionalLight)

requestID = None
progress = None
progressEnd = 6000
startTime =  None
movement = Vector3(0.02, 0.02, 0.02)

def render():
    grnMesh.position.set(0.5,0,0);
    grnMesh.scale.set(1,1,1)
    bluMesh.rotation.add(movement)
        
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