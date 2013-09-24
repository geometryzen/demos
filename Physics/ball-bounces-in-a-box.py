from browser import *
from three import *
from workbench import *

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(0x000000,1)

camera = PerspectiveCamera()

workbench3D = Workbench3D(renderer.domElement, renderer, camera)

def setUp():
    workbench3D.setUp()
    print "setUp"

def tick(t):
    renderer.render(scene, camera)

def terminate(t):
    return t > 1

def tearDown():
    print "tearDown"
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
