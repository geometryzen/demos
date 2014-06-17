from browser import *
from easel import *
from three import *
from workbench import *
from math import pow
from random import random

space3D = CartesianSpace()

workbench3D = Workbench3D(space3D.renderer.domElement, space3D.renderer, space3D.camera)

giant = SphereBuilder().color("red").radius(0.4).build()
giant.position = VectorE3(1.0, 0.0, 0.0)
giant.mass     = ScalarE3(2.0)
giant.momentum = VectorE3(0.0, -0.5, 0.0) * giant.mass
space3D.add(giant)

dwarf = SphereBuilder().color("yellow").radius(0.2).build()
dwarf.position = VectorE3(4.0, 0.0, 0.0)
dwarf.mass     = ScalarE3(1.0)
dwarf.momentum = -giant.momentum
space3D.add(dwarf)

centerOfMass = SphereBuilder().color("blue").radius(0.1).build()
space3D.add(centerOfMass)

dt = 0.02

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True


output = Text("Hit Esc to exit.", "20px Helvetica", "white")
output.x = window.innerWidth / 2
output.y = window.innerHeight / 2
space2D.addChild(output)

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()

def tick(t):
    r = dwarf.position - giant.position
    F = giant.mass * dwarf.mass * r / pow(abs(r | r), 3/2)
    impulse = F * dt
    giant.momentum += impulse
    dwarf.momentum -= impulse
    
    for star in [giant, dwarf]:
        star.position += (star.momentum / star.mass) * dt

    centerOfMass.position = (giant.position * giant.mass + dwarf.position * dwarf.mass) / (giant.mass + dwarf.mass)
    
    space3D.render()
    space2D.update()

def terminate(t):
    return t > 120

def tearDown(e):
    workbench3D.tearDown()
    workbench2D.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()
