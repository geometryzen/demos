from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *
from units import *

glwin = window.open("","","width=800,height=600")
# Changing the background color is a bit of a hack until I figure out the padding.
glwin.document.body.style.backgroundColor = "080808"
glwin.document.body.style.overflow = "hidden"
glwin.document.title = "Visualizing Rotors with WebGL"

THREE = window.THREE

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D, glwin)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text("Hit Esc key to exit.", font, "gray")
output.x = 100
output.y = 60
space2D.addChild(output)

timeOut = 60.0

camera = PerspectiveCamera(70, 1, 1, 10000)

scene = Scene()

geometry = THREE.BoxGeometry(2.0, 2.0, 2.0)

geometry.faces[0].color.setHex(0xFF0000)
geometry.faces[1].color.setHex(0xFF0000)
geometry.faces[2].color.setHex(0x00FFFF)
geometry.faces[3].color.setHex(0x00FFFF)
geometry.faces[4].color.setHex(0x00FF00)
geometry.faces[5].color.setHex(0x00FF00)
geometry.faces[6].color.setHex(0xFF00FF)
geometry.faces[7].color.setHex(0xFF00FF)
geometry.faces[8].color.setHex(0x0000FF)
geometry.faces[9].color.setHex(0x0000FF)
geometry.faces[10].color.setHex(0xFFFF00)
geometry.faces[11].color.setHex(0xFFFF00)
    
material = MeshBasicMaterial({"vertexColors": FaceColors, "overdraw": 0.5})
cube = Mesh(geometry, material)
scene.add(cube)

renderer = WebGLRenderer({"antialias": True})
renderer.setClearColor(Color(0x080808), 1.0)

space3D = CartesianSpace(scene, renderer, camera)

workbench3D = Workbench3D(renderer.domElement, renderer, camera, glwin)

tau = 2 * pi
omega = (tau / 20) / second
B1 = BivectorE3(0,0,1)
B2 = BivectorE3(0,0,0)

def tick(t):
    time = t * second
    theta = omega * time
    rotor = exp(-B2*theta.quantity/2.0) * exp(-B1*theta.quantity/2.0)
    cube.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    space3D.render()
    space2D.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench3D.setUp()
    workbench2D.setUp()

def tearDown(e):
    workbench2D.tearDown()
    workbench3D.tearDown()
    glwin.close()
    if e:
        print e

# Python does not allow functions to be referenced before they are declared.
war = WindowAnimationRunner(tick, terminate, setUp, tearDown, glwin)

war.start()
