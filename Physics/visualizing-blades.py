'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi

origin = VectorE3(0, 0, 0)
i = VectorE3(1,0,0)
space = CartesianSpace()
shape = cylinder()
# The Graphics Library uses Vector3, but Geometric Algebra uses Euclidean3.
# We'd like to have a way of not experiencing this mismatch.
shape.position.set(origin.x, origin.y, origin.z)
shape.rotateZ(pi/2)
space.add(shape)

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 10000

def setUp():
    document.removeElementsByTagName("canvas")
    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
