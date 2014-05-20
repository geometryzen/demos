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
timeOut = 6000.0

mouse = VectorE3(0.0, 10000.0, 0.5)
target = VectorE3(0.0, 200.0, 0.0)
normalMatrix = Matrix3()
ROLLOVERED = None
isShiftDown = False
isCtrlDown = False
plane = Mesh(PlaneGeometry(1000.0,1000.0), MeshBasicMaterial())

scene = Scene()
renderer = CanvasRenderer()
renderer.setClearColor(Color(0xFFFFFF), 1.0)

camera = PerspectiveCamera(70, 1, 1, 10000)
camera.position.y = 800.0

ambientLight = AmbientLight(0x606060)
scene.add(ambientLight)

light = DirectionalLight(0xFFFFFF, 2)
light.position.set(1.0, 1.0, 1.0).normalize()
scene.add(light)

light = DirectionalLight(0xFFFFFF)
light.position.set(-1.0, -1.0, -1.0).normalize()
scene.add(light)

projector = Projector()
raycaster = None

workbench = Workbench3D(renderer.domElement, renderer, camera)

def shiftKey(event, downFlag):
    global isShiftDown
    isShiftDown = downFlag

def ctrlKey(event, downFlag):
    global isCtrlDown
    isCtrlDown = downFlag

keyHandlers = {
 16: shiftKey,
 17: ctrlKey
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except:
        pass

def onDocumentKeyUp(event):
    try:
        keyHandlers[event.keyCode](event, False)
    except:
        pass

def onDocumentMouseDown(event):
    event.preventDefault()
    intersects = raycaster.intersectObjects(scene.children)
    if len(intersects) > 0:
        intersect = intersects[0]
        if isCtrlDown:
            if intersect.object != plane:
                scene.remove(intersect.object)
            pass
        else:
            normalMatrix.getNormalMatrix(intersect.object.matrixWorld)
            face = intersect.face
            if face:
                normal = face.normal.clone()
                normal.applyMatrix3(normalMatrix).normalize()
                position = intersect.point + normal
                geometry = CubeGeometry(50,50,50)
                for i in range(0, len(geometry.faces)):
                    geometry.faces[i].color.setHex(0x00ff80)
                material = MeshLambertMaterial({"vertexColors": FaceColors})
                voxel = Mesh(geometry, material)
                voxel.position.x = floor(position.x / 50.0) * 50 + 25.0
                voxel.position.y = floor(position.y / 50.0) * 50 + 25.0
                voxel.position.z = floor(position.z / 50.0) * 50 + 25.0
                voxel.matrixAutoUpdate = False
                voxel.updateMatrix()
                scene.add(voxel)

def onDocumentMouseMove(event):
    global ROLLOVERED
    event.preventDefault()
    mouse.x = (float(event.clientX) / float(window.innerWidth)) * 2.0 - 1.0
    mouse.y = - (float(event.clientY) / float(window.innerHeight)) * 2.0 + 1.0
    intersects = raycaster.intersectObjects(scene.children)
    if len(intersects) > 0:
        if ROLLOVERED:
            ROLLOVERED.color.setHex(0x00FF80)
        ROLLOVERED = intersects[0].face
        if ROLLOVERED:
            ROLLOVERED.color.setHex(0xFF8000)

def tick(t):
    global raycaster, theta
    
    if isShiftDown:
        theta += mouse.x * 3

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
        geometry.vertices.append(VectorE3(float(-size), 0.0, float(i)))
        geometry.vertices.append(VectorE3(float(+size), 0.0, float(i)))
        geometry.vertices.append(VectorE3(float(i), 0.0, float(-size)))
        geometry.vertices.append(VectorE3(float(i), 0.0, float(+size)))

    material = LineBasicMaterial({"color": 0x000000, "opacity": 0.2})
    line = Line(geometry, material, LinePieces)
    scene.add(line)
    
    plane.rotation.x = - pi / 2.0
    plane.visible = False
    scene.add(plane)
    
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
