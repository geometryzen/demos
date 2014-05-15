'''
This lesson demonstrates animating an object.
The sphere moves along a square path using coordinate instructions.
'''
from browser import WindowAnimationRunner
from geometry import CartesianSpace, SphereBuilder
from math import cos, sin, pi
from workbench import Workbench3D

L = 50
scale = 3.0/L
x = -L
y = -L
z = 0

moveX = 0
moveY = 1
moveZ = 0

space = CartesianSpace()

sphere = SphereBuilder().radius(0.1).color(0xFFFF00).build()
space.add(sphere)

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def tick(t):
    global x, y, z, moveX, moveY, moveZ
    x += moveX
    y += moveY
    z += moveZ
    if x > L:
        x = L
        moveX = 0
        moveY = -1
        moveZ = 0
    if y > L:
        y = L
        moveX = 1
        moveY = 0
        moveZ = 0
    if x < -L:
        x = -L
        moveX = 0
        moveY = 1
        moveZ = 0
    if y < -L:
        y = -L
        moveX = -1
        moveY = 0
        moveZ = 0

    sphere.position.set(x * scale, y * scale, z * scale)
    space.render()

def terminate(t):
    done = t > 10
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
