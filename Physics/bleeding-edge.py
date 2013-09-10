'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi

space = CartesianSpace()

s1 = cylinder()
s1.translateX(-2.5)
s1.translateY(-2.5)
s1.translateZ(1)
s1.rotateX(pi/2)
space.add(s1)

s2 = cube()
s2.translateX(2.5)
s2.translateY(2.5)
s2.translateZ(1)
space.add(s2)

s3 = sphere()
s3.translateX(-2.5)
s3.translateY(+2.5)
s3.translateZ(1)
space.add(s3)

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 15000

def setUp():
    document.removeElementsByTagName("canvas")
    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
