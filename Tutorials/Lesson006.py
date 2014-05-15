'''
This lesson demonstrates creating a Scene from more primitive components in the three module.
You would do this if you need more flexibility in defining the visualization.
In other words, this lesson takes us a way from Physics animations towards more realistic rendering.
Note that the object created by the SphereBuilder is really just a Mesh in the three module.
'''
from browser import document, WindowAnimationRunner
from three import Scene, PerspectiveCamera, WebGLRenderer, Color, PointLight
from geometry import SphereBuilder
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

sphere = SphereBuilder().color(0x0000FF).build()
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
