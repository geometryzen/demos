# This is a work in progress. It may not work for you yet!
# The idea is to create a simple 3D visualization library.
# The library will be similar to Visual Python.
#
# Sep 1, 2013 world, cube, cylinder, sphere
# Sep 2, 2013 WindowAnimationRunner
# TODO: Managing the size for the renderer and aspect for the camera.
from three import *
from browser import *

scene = world()

shape = cylinder()

scene.add(shape)

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(4, 4, 4)
camera.lookAt(scene.position)
camera.aspect = window.innerWidth / window.innerHeight
camera.updateProjectionMatrix()

renderer = None

movement = Vector3(0.02, 0.02, 0.02)

def cleanUp():
    for canvas in document.getElementsByTagName("canvas"):
        canvas.parentNode.removeChild(canvas)

def tick(elapsed):
    shape.rotation += movement
        
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 10000

def setUp():
    global renderer
    cleanUp()

    renderer = WebGLRenderer()
    renderer.autoClear = True
    renderer.gammaInput = True
    renderer.gammaOutput = True
    renderer.setClearColor(Color(0x080808), 1.0)

    container = document.getElementById("canvas-container")
    container.appendChild(renderer.domElement)

    renderer.size = (window.innerWidth, window.innerHeight) 


def tearDown():
"""
 tearDown is called by the animation runner when the animation is complete.
"""
    cleanUp()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
