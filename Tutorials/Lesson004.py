from browser import WindowAnimationRunner
from geometry import CartesianSpace, SphereBuilder
from math import cos, sin, pi
from workbench import Workbench

T = 5
omega = 2 * pi / T

space = CartesianSpace()

sphere = SphereBuilder().color(0x0000FF).build()
space.add(sphere)

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    sphere.position.set(cos(omega*t), sin(omega*t), 0)
    space.render()

def terminate(t):
    done = t > 4
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()