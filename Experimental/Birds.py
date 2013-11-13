from three import *
from browser import *
from workbench import *
from random import random

class Bird:
    def __init__(self):
        self.position = VectorE3(random() - 0.5, random() - 0.5, random() - 0.5) * 400.0
        self.velocity = VectorE3(random() - 0.5, random() - 0.5, random() - 0.5) * 2.0
        self._avoidWalls = False
        self._width  = 500
        self._height = 500
        self._depth  = 500

    def setAvoidWalls(self, avoidWalls):
        self._avoidWalls = avoidWalls

    def setWorldSize(self, width, height, depth):
        self._width  = width
        self._height = height
        self._depth  = depth
        
def birdMesh():
    g = Geometry();
    m = MeshBasicMaterial({"color": random() * 0xFFFFFF, "side": DoubleSide})

# global timeOut allows us to terminate the program gracefully on time or Esc key.
timeOut = 5

# Don't need to set the aspect for the camera - the workbench will do that.
camera = PerspectiveCamera(75.0, 1.0, 1.0, 10000.0)
camera.position.z = 450

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0xFFFFFF), 1.0)

workbench3D = Workbench3D(renderer.domElement, renderer, camera)

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

birds = []
    
def setUp():
    for i in range(0, 200):
        bird = Bird()
        bird.setAvoidWalls(True)
        bird.setWorldSize(200, 200, 200)
        birds.append(bird)
        
    workbench3D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def render(t):
    try:
        renderer.render(scene, camera)
    except:
        print "Unexpected error"

def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()

WindowAnimationRunner(render, terminate, setUp, tearDown).start()
