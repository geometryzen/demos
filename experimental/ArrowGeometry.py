# Under Construction
# ArrowGeometry demonstration.
from eight import *
from browser import *
from math import pi

for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 200

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

length = 100
radiusShaft = 5
radiusCone = radiusShaft * 2
lengthCone = radiusCone * 2
lengthShaft = length - lengthCone
a = Vector3(0, 0, length)
b = Vector3(radiusCone, 0, lengthShaft)
c = Vector3(radiusShaft, 0, lengthShaft)
d = Vector3(radiusShaft, 0, 0)
e = Vector3(0, 0, 0)
points = [a, b, c, d, e]
arrow = LatheGeometry(points, 4)

redLamb = MeshLambertMaterial({"color":0xFF0000})
redWire = MeshBasicMaterial({"color":0xFF0000, "wireframe":True, "wireframeLinewidth":3})
bluWire = MeshBasicMaterial({"color":0x0000FF, "wireframe":True, "wireframeLinewidth":3})
redArrow = Mesh(arrow, redWire)
bluArrow = Mesh(arrow, bluWire)
scene.add(redArrow)
scene.add(bluArrow)

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
    bluArrow.rotation.add(movement)
        
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