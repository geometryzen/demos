'''
The binary star problem with scaling.
'''
from browser import *
from easel import *
from three import *
from workbench import *
from math import pow
from random import random

space3D = CartesianSpace()

workbench3D = Workbench(space3D.renderer, space3D.camera)

giant = SphereBuilder().color("red").radius(0.4).build()
giant.position = VectorE3(-2, 0, 0)
giant.mass     = ScalarE3(2)
giant.momentum = VectorE3(0, -0.5, 0) * giant.mass
space3D.add(giant)

dwarf = SphereBuilder().color("yellow").radius(0.2).build()
dwarf.position = VectorE3(4, 0, 0)
dwarf.mass     = ScalarE3(1)
dwarf.momentum = -giant.momentum
space3D.add(dwarf)

dt = 0.02

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

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()

def tick(t):
    r = dwarf.position - giant.position
    F = giant.mass * dwarf.mass * r / pow(r % r, 3/2)
    giant.momentum = giant.momentum + F * dt
    dwarf.momentum = dwarf.momentum - F * dt
    
    for star in [giant, dwarf]:
        star.position = star.position + (star.momentum / star.mass) * dt
    
    space3D.render()
    space2D.update()

def terminate(t):
    return t > 120

def tearDown():
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
