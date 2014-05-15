'''
boilerplate code for creating a 3D simulation.
'''
from three import *
from browser import *
from workbench import *

# global timeOut allows us to terminate the program gracefully on time or Esc key.
timeOut = 5

# Don't need to set the aspect for the camera - the workbench will do that.
camera = PerspectiveCamera(75.0, 1.0, 1.0, 10000.0)
camera.position.z = 450

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

workbench3D = Workbench3D(renderer.domElement, renderer, camera, window)

def setUp():
    workbench3D.setUp()

def render(t):
    try:
        renderer.render(scene, camera)
    except:
        print "Unexpected error"

def terminate(t):
    return t > timeOut

def tearDown(e):
    workbench3D.tearDown()
    print e

WindowAnimationRunner(render, terminate, setUp, tearDown).start()
