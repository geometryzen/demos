'''
This lesson demonstrates animating an object.
The sphere moves along a square path using geometric instructions.
'''
from browser import WindowAnimationRunner
from e3ga import *
from geometry import CartesianSpace, SphereBuilder
from math import sqrt
from workbench import Workbench

L = 50
scale = 3.0 / L

i = VectorE3(1, 0, 0, False)
j = VectorE3(0, 1, 0, False)
k = VectorE3(0, 0, 1, False)

position = -L * i -L * j
move = j.clone()
R = (1 + i * j) / sqrt(2)

space = CartesianSpace()

sphere = SphereBuilder().radius(0.1).color(0xFFFF00).build()
space.add(sphere)

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    global position
    position += move
    if position % i > L:
        position = position - (i << position) * i + (L * i)
        move = R * move * ~R
    if position.y > L:
        position.y = L
        move.x = 1
        move.y = 0
        move.z = 0
    if position.x < -L:
        position.x = -L
        move.x = 0
        move.y = 1
        move.z = 0
    if position.y < -L:
        position.y = -L
        move.x = -1
        move.y = 0
        move.z = 0

    sphere.position.set(position.x * scale, position.y * scale, position.z * scale)
    space.render()

def terminate(t):
    done = t > 10
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
