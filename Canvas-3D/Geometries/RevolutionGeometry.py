'''
This will be temporarily broken while issues relating to rotation axis and attitude are resolved.
RevolutionGeometry will fix issues in LatheGeometry.
'''
from geometry import *
from three import *
from browser import *
from workbench import *

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
# The points are to be rotated in the xy-plane to generate the geometry.
generator = BivectorE3(1, 0, 0)
arrow = RevolutionGeometry(points, generator, 12)

material = MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3})
mesh = Mesh(arrow, material)
space.add(mesh)

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    space.render()
    
def terminate(t):
    return t > 3

def setUp():
    workbench.setUp()
    space.camera.position.set(1.5, 1.5, 1.5)
    space.camera.lookAt(space.origin)

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
