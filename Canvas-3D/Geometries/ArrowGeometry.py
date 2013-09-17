# ArrowGeometry is not a standard Geometry in the Three.js library.
from three import *
from browser import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 1.3

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

# All arguments are optional and the defaults, in order, are as follows.
length = 1
segments = 12
radiusShaft = 0.01
radiusCone = 0.08
lengthCone = 0.2
arrow = ArrowGeometry(length, segments)

material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 3})
mesh = Mesh(arrow,material)
scene.add(mesh)

movement = Vector3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def tick(elapsed):
    mesh.rotation += movement
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 12000

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
