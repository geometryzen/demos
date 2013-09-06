# TODO: We don't want world and shapes to come from three anymore.
from geometry import Scene, CartesianSpace, world, cylinder, PerspectiveCamera, WebGLRenderer, Color, Vector3
from browser import document, window, WindowAnimationRunner

space = CartesianSpace(world())

shape = cylinder()
space.add(shape)

space.renderer.setClearColor(Color(0x080808), 1.0)
container = None

movement = Vector3(0.02, 0.02, 0.02)

def discardCanvasElements():
    for element in document.getElementsByTagName("canvas"):
        element.parentNode.removeChild(element)

def tick(elapsed):
    shape.rotation += movement
    space.renderer.render(space.scene, space.camera)
    
def terminate(elapsed):
    return elapsed > 6000

def setUp():

    discardCanvasElements()

    document.body.insertBefore(renderer.domElement, document.body.firstChild)
    space.renderer.size = (window.innerWidth, window.innerHeight)
    space.camera.aspect = window.innerWidth / window.innerHeight
    space.camera.updateProjectionMatrix()

def tearDown():
    discardCanvasElements()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
