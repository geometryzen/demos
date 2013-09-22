# ArrowGeometry is not a standard Geometry in the Three.js library.
from three import *
from browser import *
from workbench import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 1.3

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

# All arguments are optional and the defaults, in order, are as follows.
length = 1
segments = 12
radiusShaft = 0.01
radiusCone = 0.08
lengthCone = 0.2
arrow = ArrowGeometry(length)
arrow.name = 'Foo'

print repr(arrow)
print "uuid:            " + str(arrow.uuid)
print "name:            " + str(arrow.name)
print arrow

material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 3})
mesh = Mesh(arrow, material)
scene.add(mesh)

movement = 0.02 * VectorE3(1, 1, 1)

workbench = Workbench(renderer, camera)

def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 3

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
