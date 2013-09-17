# RevolutionGeometry is not a standard Geometry in the Three.js library.
# It is an experimental enhancement to LatheGeometry for closed surfaces of revolution.
from geometry import *
from three import *
from browser import *

space = CartesianSpace()

# All arguments are optional and the defaults, in order, are as follows.
radiusCone = 0.08
lengthCone = 0.2
radiusShaft = 0.01
length = 1
lengthShaft = 1 - lengthCone
a = Vector3(0, 0, length)
b = Vector3(radiusCone, 0, lengthShaft)
c = Vector3(radiusShaft, 0, lengthShaft)
d = Vector3(radiusShaft, 0, 0)
e = Vector3(0, 0, 0)
points = [a, b, c, d, e]
arrow = RevolutionGeometry(points, 25)

material = MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3})
mesh = Mesh(arrow, material)
scene.add(mesh)

movement = Vector3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def tick(elapsed):
    mesh.rotation += movement
    space.render()
    
def terminate(elapsed):
    return elapsed > 12000

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
