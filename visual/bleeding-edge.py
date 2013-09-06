# TODO: We don't want world and shapes to come from three anymore.
from geometry import Scene, CartesianSpace, world, cylinder, PerspectiveCamera, WebGLRenderer, Color, Vector3
from browser import document, window, WindowAnimationRunner

scene = world()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(8, 8, 8)

space = CartesianSpace(scene, camera)

shape = cylinder()
space.add(shape)

camera.lookAt(space.origin)

renderer = None
container = None

movement = Vector3(0.02, 0.02, 0.02)

def discardCanvasElements():
    for element in document.getElementsByTagName("canvas"):
        element.parentNode.removeChild(element)

def tick(elapsed):
    shape.rotation += movement
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 6000

def setUp():
    global renderer

    discardCanvasElements()

    renderer = WebGLRenderer()
    renderer.setClearColor(Color(0x080808), 1.0)

    document.body.insertBefore(renderer.domElement, document.body.firstChild)
    renderer.size = (window.innerWidth, window.innerHeight)
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()

def tearDown():
    discardCanvasElements()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
