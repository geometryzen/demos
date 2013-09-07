from geometry import *
from browser import *

space = CartesianSpace()
space.add(cylinder())

def discardCanvasElements():
    for element in document.getElementsByTagName("canvas"):
        element.parentNode.removeChild(element)

def setUp():
    discardCanvasElements()

    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 6000

def tearDown():
    discardCanvasElements()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
