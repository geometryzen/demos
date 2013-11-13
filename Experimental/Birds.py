from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *

# global timeOut allows us to terminate the program gracefully on time or Esc key.
timeOut = 10

# Don't need to set the aspect for the camera - the workbench will do that.
camera = PerspectiveCamera(75, 1, 1, 10000)
camera.position.z = 450

scene = Scene()

renderer = WebGLRenderer()

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

def setUp():
    workbench3D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def render(t):
    try:
        space3D.render()
    except:
        pass

def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()

WindowAnimationRunner(render, terminate, setUp, tearDown).start()