from browser import *
from geometry import *
from math import *
from workbench import *

T = 5 # Periodic Time
omega = 2 * pi / T # Angular Velocity
R = 4 # radius

scene = Scene()

renderer = WebGLRenderer({"antialias":True})

space = CartesianSpace(scene, renderer)

sphere = SphereBuilder().color(0x0000FF).build()
space.add(sphere)

workbench = Workbench3D(renderer.domElement, renderer, space.camera)

timeOut = 1.5 * T

def tick(t):
    sphere.position.set(R * cos(omega*t), R * sin(omega*t), 0)
    space.render()

def terminate(time):
    return time > timeOut

def setUp():
    workbench.setUp()

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
