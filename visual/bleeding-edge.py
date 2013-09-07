from geometry import *
from browser import *

space = CartesianSpace()
space.add(sphere())

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def setUp():
    document.removeElementsByTagName("canvas")
    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 6000

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
