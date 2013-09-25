from three import *
from browser import *
from workbench import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

radiusCone = 20
radiusShaft = 10
length = 80
lengthShaft = 60
a = VectorE3(0, 0, length)
b = VectorE3(radiusCone, 0, lengthShaft)
c = VectorE3(radiusShaft, 0, lengthShaft)
d = VectorE3(radiusShaft, 0, 0)
e = VectorE3(0, 0, 0)
points = [a, b, c, d, e]
arrow = LatheGeometry(points, 25)

material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 3})
mesh = Mesh(arrow, material)
scene.add(mesh)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 10

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
