from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *
from units import *

THREE = window.THREE

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
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

workbench3D = Workbench3D(renderer.domElement, renderer, camera)

tau = 2 * pi
omega = (tau / 20) / second
# A unit bivector rotating from k to i
B = BivectorE3(1.0, 0.0, 0.0)
# Just make sure that we really do have a unit bivector.
B = B / magnitude(B)

def tick(t):
    time = t * second
    theta = omega * time
    # The rotor is defined to have a minus sign.
    rotor = exp(-B*theta.quantity/2.0)
    theta = pi / 2
    B1 = BivectorE3(0,0,1)
    B2 = BivectorE3(0,1,0)
    rotor = exp(-B2*theta/2.0) * exp(-B1*theta/2.0)
    rotor = exp(-(B1 + B2)*theta/2.0)
    print magnitude(rotor)
    # Unfortunately, we have to use a minus sign to convert the rotor grade 2 components to the quaternion values.
    cube.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    # cube.attitude = rotor
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
    if e:
        print e

# Python does not allow functions to be referenced before they are declared.
war = WindowAnimationRunner(tick, terminate, setUp, tearDown)

war.start()
