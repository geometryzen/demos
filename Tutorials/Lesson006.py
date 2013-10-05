from browser import document, WindowAnimationRunner
from three import Scene, PerspectiveCamera, WebGLRenderer, Color
from geometry import SphereBuilder
from math import cos, sin, pi
from workbench import Workbench

T = 5
omega = 2 * pi / T
R = 4

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

sphere = SphereBuilder().wireframe(True).color(0x0000FF).build()
scene.add(sphere)

workbench = Workbench(renderer, camera)

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
