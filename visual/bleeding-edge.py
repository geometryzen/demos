from geometry import *
from browser import *

space = CartesianSpace()
space.add(cylinder())

def discardCanvasElements():
    for element in document.getElementsByTagName("canvas"):
        element.parentNode.removeChild(element)

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def setUp():
    discardCanvasElements()
    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 15000

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    discardCanvasElements()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
