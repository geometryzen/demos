'''
This lesson demonstrates constructing a Mesh from a Geometry and Material.
This gives you more control over the visual appearance of the Mesh objects in your scene.
'''
from browser import document, WindowAnimationRunner
from three import Scene, PerspectiveCamera, WebGLRenderer, Color, PointLight, SphereGeometry, MeshNormalMaterial, Mesh
from math import cos, sin, pi
from workbench import Workbench3D

T = 5
omega = 2 * pi / T
R = 4

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 10
camera.lookAt(scene.position)

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

pointLight = PointLight(0xFFFFFF, 1, 100)
pointLight.position.set(0, 0, 10)
scene.add(pointLight)

geometry = SphereGeometry(1.0)
material = MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3})
sphere = Mesh(geometry, material)
scene.add(sphere)

workbench = Workbench3D(renderer.domElement, renderer, camera)

timeOut = 20

def tick(t):
    sphere.position.set(R * cos(omega*t), R * sin(omega*t), 0)
    renderer.render(scene, camera)

def terminate(t):
    done = t > timeOut
    return done

def setUp():
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()
    
def escKey(event, downFlag):
    event.preventDefault()
    global timeOut
    timeOut = 0

keyHandlers = {
 27: escKey
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except:
        pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
