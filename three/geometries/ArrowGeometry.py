# ArrowGeometry is not a standard Geometry in the Three.js library.
# It is created from the LatheGeometry using a set of points that create the cone and shaft
# of an arrow.
from three import *
from browser import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 1.3

renderer = None

# All arguments are optional and the defaults are as follows.
length = 1
segments = 12
radiusShaft = 0.01
radiusCone = 0.08
lengthCone = 0.2
arrow = ArrowGeometry(length, segments, radiusShaft, radiusCone, lengthCone)

material = MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3})
mesh = Mesh(arrow,material)
scene.add(mesh)

ambientLight = AmbientLight(0x222222)
scene.add(ambientLight)

pointLight = PointLight(0xFFFFFF)
pointLight.position.set(20, 20, 20)
scene.add(pointLight)

directionalLight = DirectionalLight(0xFFFFFF)
directionalLight.position.set(0, 1, 0)
scene.add(directionalLight)

movement = Vector3(0.02, 0.02, 0.02)

def onWindowResize(event):
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)
    
window.addEventListener("resize", onWindowResize, False)

onWindowResize(None)

def removeElementsByTagName(tagName):
    for element in document.getElementsByTagName(tagName):
        element.parentNode.removeChild(element)

def tick(elapsed):
    shape.rotation += movement
        
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 10000

def setUp():
    global renderer

    removeElementsByTagName("canvas")

    renderer = WebGLRenderer()
    renderer.autoClear = True
    renderer.gammaInput = True
    renderer.gammaOutput = True
    renderer.setClearColor(Color(0x080808), 1.0)

    document.getElementById("canvas-container").appendChild(renderer.domElement)

    renderer.size = (window.innerWidth, window.innerHeight) 


def tearDown():
    removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
