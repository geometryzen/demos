'''
This lesson demonstrates animating an object.
The sphere performs cirular motion with radius R and periodic time T.
'''
from browser import WindowAnimationRunner
from geometry import CartesianSpace, SphereBuilder
from math import cos, sin, pi
from workbench import Workbench3D

T = 5
omega = 2 * pi / T
R = 4

space = CartesianSpace()

sphere = SphereBuilder().color(0x0000FF).build()
space.add(sphere)

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def tick(t):
    sphere.position.set(R * cos(omega*t), R * sin(omega*t), 0.0)
    space.render()

def terminate(t):
    done = t > 10
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
