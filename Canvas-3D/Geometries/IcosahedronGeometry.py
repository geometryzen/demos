# IcosahedronGeometry demonstration.
from three import *
from browser import *
from math import pi

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

radius = 1
detail = 0 # Must be an integer: 0,1,2,...

icosa = IcosahedronGeometry(radius, detail)

print repr(icosa)
print "radius:         " + str(icosa.radius)
print "detail:         " + str(icosa.detail)
print icosa

mesh = Mesh(icosa, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

requestID = None
progress = None
progressEnd = 10000
startTime =  None
movement = Vector3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def render():
    mesh.rotation += movement
        
    renderer.render(scene, camera)

def onWindowResize(event):
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

onWindowResize(None)
workbech.setUp()
step(None)