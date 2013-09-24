'''
Looks like we may have some scaling problems here.
'''
from browser import *
from three import *
from workbench import *
from math import pow
from random import random

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

camera = PerspectiveCamera(50,1,0.1, 1e30)
camera.position.z = 1e11

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
dt = 1e5

def setUp():
    workbench3D.setUp()

def tick(t):
    r = dwarf.position - giant.position
    F = G * giant.mass * dwarf.mass * r / pow(r % r, 3/2)
    giant.momentum += F * dt
    dwarf.momentum -= F * dt
    
    for star in [giant, dwarf]:
        star.position += (star.momentum / star.mass) * dt
    
    renderer.render(scene, camera)

def terminate(t):
    return t > 100

def tearDown():
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
