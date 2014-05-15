'''
This lesson demonstrates animating an object.
The sphere moves along a square path using geometric instructions.
'''
from browser import WindowAnimationRunner
from e3ga import *
from geometry import CartesianSpace, SphereBuilder
from math import sqrt
from workbench import Workbench3D

L = 50.0
scale = 4.0 / L

i = VectorE3(1.0, 0.0, 0.0, False)
j = VectorE3(0.0, 1.0, 0.0, False)
k = VectorE3(0.0, 0.0, 1.0, False)

position = (L * i + L * j) * -1.0
move = j.clone()
R = (1.0 + i * j) / sqrt(2)

space = CartesianSpace()

sphere = SphereBuilder().radius(0.1).color(0xFFFF00).build()
space.add(sphere)

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def tick(t):
    global position, move
    position += move
    if (position % i).w > L:
        position = position + L * i - (i << position) * i
        move = R * move * ~R
        return
    if (position % j).w > L:
        position = position - (j << position) * j + (L * j)
        move = R * move * ~R
        return
    if (position % i).w < -L:
        position = position - (i << position) * i - (L * i)
        move = R * move * ~R
        return
    if (position % j).w < -L:
        position = position - (j << position) * j - (L * j)
        move = R * move * ~R
        return

    sphere.position = position * scale
    space.render()

def terminate(t):
    done = t > 15
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
