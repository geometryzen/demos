'''
Looks like we may have some scaling problems here.
'''
from browser import *
from easel import *
from three import *
from workbench import *
from math import pow
from random import random

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

camera = PerspectiveCamera(50,1,0.1, 1e30)
camera.position.z = 1e12

pointLight = PointLight(0xFFFFFF);
pointLight.position = camera.position
scene.add(pointLight)

workbench3D = Workbench(renderer, camera)

giant = SphereBuilder().color("red").radius(4e10).build()
giant.position = VectorE3(-1e11, 0, 0)
giant.mass     = ScalarE3(2e30)
giant.momentum = VectorE3(0, 0, -1e4) * giant.mass
scene.add(giant)

dwarf = SphereBuilder().color("yellow").radius(2e10).build()
dwarf.position = VectorE3(1.5e11, 0, 0)
dwarf.mass     = ScalarE3(1e30)
dwarf.momentum = -giant.momentum
scene.add(dwarf)

G = 6.7e-11
dt = 0.05

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
    F = G * giant.mass * dwarf.mass * r / pow(r % r, 3/2)
    giant.momentum += F * dt
    dwarf.momentum -= F * dt
    
    for star in [giant, dwarf]:
        star.position += (star.momentum / star.mass) * dt
    
    output.text = repr(F)
    
    renderer.render(scene, camera)
    space2D.update()

def terminate(t):
    return t > 60

def tearDown():
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
