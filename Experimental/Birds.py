from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *

# Don't need to set the aspect for the camera - the workbench will do that.
camera = new PerspectiveCamera(75, 1, 1, 10000)
camera.position.z = 450

scene = Scene()

renderer = CanvasRenderer()

canvas3D = space3D.renderer.domElement
workbench3D = Workbench3D(canvas3D, space3D.renderer, space3D.camera)

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