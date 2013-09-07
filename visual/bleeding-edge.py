from geometry import *
from browser import *

space = CartesianSpace()
space.add(cylinder())

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def setUp():
    document.removeElementsByTagName(123)#"canvas")
    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 10000

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
