from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *

THREE = window.THREE

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text("Drag to spin the cube. Hit Esc key to exit.", font, "gray")
output.x = 100
output.y = 60
space2D.addChild(output)

timeOut = 60.0

mouseX = 0
mouseXOnMouseDown = 0
targetRotation = 0
targetRotationOnMouseDown = 0
isShiftDown = False
isCtrlDown = False

camera = PerspectiveCamera(70, 1, 1, 10000)
camera.position.y = 150.0
camera.position.z = 500.0

scene = Scene()

geometry = BoxGeometry(200.0, 200.0, 200.0)
for i in range(0, len(geometry.faces), 2):
    print i
    hex = int(random() * 0xFFFFFF)
    geometry.faces[i].color.setHex(hex)
    geometry.faces[i+1].color.setHex(hex)
geometry.faces[0].color.setHex(0xFF0000)
geometry.faces[1].color.setHex(0xFF0000)
geometry.faces[2].color.setHex(0x00FF00)
geometry.faces[3].color.setHex(0x00FF00)
geometry.faces[4].color.setHex(0x0000FF)
geometry.faces[5].color.setHex(0x0000FF)
    
material = MeshBasicMaterial({"vertexColors": FaceColors, "overdraw": 0.5})
cube = Mesh(geometry, material)
cube.position.y = 150.0
scene.add(cube)

geometry = PlaneGeometry(200.0, 200.0)
geometry.applyMatrix(Matrix4().makeRotationX(-pi / 2.0))
material = MeshBasicMaterial({"color": 0xE0E0E0, "overdraw": 0.5})
plane = Mesh(geometry, material)
scene.add(plane)

renderer = WebGLRenderer({"antialias": True})
renderer.setClearColor(Color(0x080808), 1.0)

workbench = Workbench3D(renderer.domElement, renderer, camera)

CartesianSpace(scene, renderer)

def onDocumentMouseDown(event):
    global mouseXOnMouseDown, targetRotationOnMouseDown

    event.preventDefault()

    document.addEventListener("mousemove", onDocumentMouseMove, False)
    document.addEventListener("mouseup", onDocumentMouseUp, False)
    document.addEventListener("mouseout", onDocumentMouseOut, False)

    mouseXOnMouseDown = event.clientX - (float(window.innerWidth) / 2.0)
    targetRotationOnMouseDown = targetRotation
    
def onDocumentMouseMove(event):
    global mouseX, targetRotation

    mouseX = event.clientX - (float(window.innerWidth) / 2.0)
    targetRotation = targetRotationOnMouseDown + (mouseX - mouseXOnMouseDown) * 0.02

def onDocumentMouseUp(event):
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("mouseup", onDocumentMouseUp, False)
    document.removeEventListener("mouseout", onDocumentMouseOut, False)

def onDocumentMouseOut(event):
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("mouseup", onDocumentMouseUp, False)
    document.removeEventListener("mouseout", onDocumentMouseOut, False)

def tick(t):
    
    cube.rotation.y += (targetRotation - cube.rotation.y) * 0.05
    plane.rotation.y = cube.rotation.y
    renderer.render(scene, camera)
    space2D.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench.setUp()
    workbench2D.setUp()
    document.addEventListener("mousedown", onDocumentMouseDown, False)

def tearDown():
    document.removeEventListener("mousedown", onDocumentMouseDown, False)
    workbench2D.tearDown()
    workbench.tearDown()

# Python does not allow functions to be referenced before they are declared.
war = WindowAnimationRunner(tick, terminate, setUp, tearDown)

war.start()
