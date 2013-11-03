from three import *
from browser import *
from workbench import *

scene = Scene()
renderer = WebGLRenderer()
renderer.sortObjects = False
camera = PerspectiveCamera(70, 1, 1, 10000)

light = DirectionalLight(0xFFFFFF, 2)
light.position.set(1, 1, 1).normalize()
scene.add(light)


workbench = Workbench(renderer, camera)

def tick(t):
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 4

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
