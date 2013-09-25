from three import *
from browser import *
from workbench import *

space = CartesianSpace()

radiusCone = 0.20
radiusShaft = 0.10
length = 0.80
lengthShaft = 0.60
a = VectorE3(0, 0, length)
b = VectorE3(radiusCone, 0, lengthShaft)
c = VectorE3(radiusShaft, 0, lengthShaft)
d = VectorE3(radiusShaft, 0, 0)
e = VectorE3(0, 0, 0)
points = [a, b, c, d, e]
arrow = LatheGeometry(points, 25)

material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 3})
mesh = Mesh(arrow, material)
space.add(mesh)

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(t):
    space.render()
    
def terminate(t):
    return t > 10

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
