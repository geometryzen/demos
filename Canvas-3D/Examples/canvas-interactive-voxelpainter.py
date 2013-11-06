'''
Under Construction. Nov 5, 2013
'''
from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text("Hit Esc key to exit.", font, "black")
output.x = 100
output.y = 60
space2D.addChild(output)

radius = 100.0
theta = 45.0
timeOut = 60.0

mouse = VectorE3(0, 10000, 0.5)
target = VectorE3(0,200,0)
ROLLOVERED = None
isShiftDown = False
isCtrlDown = False

scene = Scene()
renderer = CanvasRenderer()

camera = PerspectiveCamera(70, 1, 1, 10000)
camera.position.y = 800

light = DirectionalLight(0xFFFFFF, 2)
light.position.set(1, 1, 1).normalize()
scene.add(light)

light = DirectionalLight(0xFFFFFF)
light.position.set(-1, -1, -1).normalize()
scene.add(light)

projector = Projector()
raycaster = None

workbench = Workbench(renderer, camera)

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

def onDocumentKeyUp(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except:
        pass

def onDocumentMouseDown(event):
    event.preventDefault()
    intersects = raycaster.intersectObjects(scene.children)
    if len(intersects) > 0:
        intersect = intersects[0]
        if isCtrlDown:
            pass
        else:
            normalMatrix.getNormalMatrix(intersect.object.matrixWorld)

def onDocumentMouseMove(event):
    event.preventDefault()
    mouse.x = (float(event.clientX) / float(window.innerWidth)) * 2.0 - 1.0
    mouse.y = - (float(event.clientY) / float(window.innerHeight)) * 2.0 + 1.0
    intersects = raycaster.intersectObjects(scene.children)
    if len(intersects) > 0:
        if ROLLOVERED:
            ROLLOVERED.color.setHex(0x00FF80)
        ROLLOVERED = intersects[0].face
        ROLLOVERED.color.setHex(0xFF8000)

def tick(t):
    global raycaster

    camera.position.x = 1400.0 * sin(theta * pi / 360.0)
    camera.position.z = 1400.0 * cos(theta * pi / 360.0)
    camera.lookAt(target)
    
    raycaster = projector.pickingRay(mouse.clone(), camera)
    
    renderer.render(scene, camera)
    space2D.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    geometry = Geometry()
    size = 500
    step = 50
    for i in range(-size, size + 1, step):
        print i
    workbench.setUp()
    workbench2D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)
    document.addEventListener("mousemove", onDocumentMouseMove, False)
    document.addEventListener("mousedown", onDocumentMouseDown, False)

def tearDown():
    document.removeEventListener("mousedown", onDocumentMouseDown, False)
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench2D.tearDown()
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
