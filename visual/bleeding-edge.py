from geometry import CartesianSpace, cylinder
from browser import document, window, WindowAnimationRunner

space = CartesianSpace()

space.add(cylinder())

def discardCanvasElements():
    for element in document.getElementsByTagName("canvas"):
        element.parentNode.removeChild(element)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 6000

def setUp():

    discardCanvasElements()

    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    #space.viewSize(window.innerWidth, window.innerHeight);
    space.renderer.setSize(window.innerWidth, window.innerHeight)
    space.camera.aspect = window.innerWidth / window.innerHeight
    space.camera.updateProjectionMatrix()

def tearDown():
    discardCanvasElements()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
