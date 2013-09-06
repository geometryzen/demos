from geometry import CartesianSpace, cylinder, Vector3
from browser import document, window, WindowAnimationRunner

space = CartesianSpace()

shape = cylinder()
space.add(shape)

container = None

movement = Vector3(0.02, 0.02, 0.02)

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
    space.renderer.size = (window.innerWidth, window.innerHeight)
    space.camera.aspect = window.innerWidth / window.innerHeight
    space.camera.updateProjectionMatrix()

def tearDown():
    discardCanvasElements()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
