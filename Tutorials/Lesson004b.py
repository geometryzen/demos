'''
This lesson demonstrates animating an object.
The sphere moves along a square path using geometric instructions.
'''
from browser import WindowAnimationRunner
from e3ga import *
from geometry import CartesianSpace, SphereBuilder
from math import cos, sin, pi
from workbench import Workbench

L = 50
scale = 3.0/L

i = VectorE3(1,0,0, False)
j = VectorE3(0,1,0, False)

position = -L * i -L * j
move = j.clone()

space = CartesianSpace()

sphere = SphereBuilder().radius(0.1).color(0xFFFF00).build()
space.add(sphere)

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    position.x += move.x
    position.y += move.y
    position.z += move.z
    if position.x > L:
        position.x = L
        move.x = 0
        move.y = -1
        move.z = 0
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
