# This is a work in progress. It may not work for you yet!
# The idea is to create a simple 3D visualization library.
# The library will be similar to Visual Python.
#
# Sep 1, 2013 world, cube, cylinder, sphere
# Sep 2, 2013 WindowAnimationRunner
# TODO: Managing the size for the renderer and aspect for the camera.
# TODO: Shape color and name.
from three import *
from browser import *

scene = world()

shape = cube()

scene.add(shape)

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(8, 8, 8)
camera.lookAt(scene.position)

renderer = None
container = None

movement = Vector3(0.02, 0.02, 0.02)

def removeElementsByTagName(tagName):
    for element in document.getElementsByTagName(tagName):
        element.parentNode.removeChild(element)

def tick(elapsed):
    """
    Called by the animation runner for each animation frame.
    """
    shape.rotation += movement
        
    renderer.render(scene, camera)
    
def terminate(elapsed):
    """
    Called by the animation runner to determine if the animation should terminate.
    """
    return elapsed > 10000

def setUp():
    """
    Called by the animation runner before the animation has started.
    """
    global renderer

    removeElementsByTagName("canvas")

    renderer = WebGLRenderer()
    renderer.autoClear = True
    renderer.gammaInput = True
    renderer.gammaOutput = True
    renderer.setClearColor(Color(0x080808), 1.0)

    container = document.getElementById("canvas-container")
    container.appendChild(renderer.domElement)
    print (container.offsetWidth, container.offsetHeight)
#   renderer.size = (window.innerWidth, window.innerHeight) 
    renderer.size = (container.offsetWidth, container.offsetHeight) 
    camera.aspect = container.offsetWidth / container.offsetHeight
    camera.updateProjectionMatrix()


def tearDown():
    """
    Called by the animation runner after the animation has finished.
    """
    removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
