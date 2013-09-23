from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *
from math import exp, pi

space3D = CartesianSpace()
canvas3D = space3D.renderer.domElement
workbench3D = Workbench3D(canvas3D, space3D.renderer, space3D.camera)
   
canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

output = Text("", "20px Helvetica", "white")
output.x = window.innerWidth / 2
output.y = window.innerHeight / 2
space2D.addChild(output)

quantity = Euclidean3(1, 2, 3, 4, 5, 6, 7, 8)
sphere = SphereBuilder.wireframe(True).build()
rotor = exp(-BivectorE3(0,0,1)*pi/4)
arrow = ArrowBuilder().wireframe(True).color(0xFFFF00).attitude(rotor).build()
arrow = ArrowBuilder().wireframe(True).color(0xFFFF00).attitude(rotor).build()
probe = ProbeE3(sphere, arrow)

#space3D.add(probe.sphere)
space3D.add(probe.arrow)

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()

def tick(t):
    probe.quantity = quantity
    output.text = repr(probe.quantity)
    space3D.render()
    space2D.update()

def terminate(t):
    return t > 6

def tearDown():
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
