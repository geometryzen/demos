'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *

space = CartesianSpace()
shape = cylinder()
space.add(shape)

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 16000

def setUp():
    document.removeElementsByTagName("canvas")
    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
