from browser import *
from easel import *
from three import *
from workbench import *
from math import pow
from random import random

space3D = CartesianSpace()

workbench3D = Workbench3D(space3D.renderer.domElement, space3D.renderer, space3D.camera)

giant = ConeBuilder().color("red").volume(0.1).build()
giant.position = VectorE3(1, 0, 0)
giant.mass     = ScalarE3(2)
giant.momentum = VectorE3(0, -0.5, 0) * giant.mass
space3D.add(giant)

dwarf = CubeBuilder().color("yellow").volume(0.1).build()
dwarf.position = VectorE3(4, 0, 0)
dwarf.mass     = ScalarE3(1)
dwarf.momentum = -giant.momentum
space3D.add(dwarf)

blob = CylinderBuilder().color("blue").volume(0.11).build()
space3D.add(blob)

dt = 0.02

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True


output = Text("Hit Esc key to exit the animation.", "20px Helvetica", "white")
output.x = window.innerWidth / 2
output.y = window.innerHeight / 2
space2D.addChild(output)

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()

def tick(t):
    r = dwarf.position - giant.position
    F = giant.mass * dwarf.mass
    F = F * r
    F = F / pow(abs(r * r), 3/2)
    giant.momentum = giant.momentum + F * dt
    dwarf.momentum = dwarf.momentum - F * dt
    
    for star in [giant, dwarf]:
        star.position = star.position + (star.momentum / star.mass) * dt

    blob.position = (giant.position * giant.mass + dwarf.position * dwarf.mass) / (giant.mass + dwarf.mass)
    
    space3D.render()
    space2D.update()

def terminate(t):
    return t > 120

def tearDown(e):
    workbench3D.tearDown()
    workbench2D.tearDown()
    print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()

