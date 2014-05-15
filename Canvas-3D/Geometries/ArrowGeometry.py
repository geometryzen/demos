from three import *
from browser import *
from workbench import *

e3 = VectorE3(0.0, 0.0, 1.0, False)

space = CartesianSpace()

# All arguments are optional and the defaults, in order, are as follows.
scale = 6.0
length = 1.0
segments = 12
radiusShaft = 0.01
radiusCone = 0.08
lengthCone = 0.2
geometry = ArrowGeometry(scale, ScalarE3(1.0), segments, length, radiusShaft, radiusCone, lengthCone, e3)
material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1})
arrow = Mesh(geometry, material)
arrow.geometry.name = 'Foo'

print repr(geometry)
print "uuid:            " + str(arrow.geometry.uuid)
print "name:            " + str(arrow.geometry.name)
print geometry

space.add(arrow)

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def tick(t):
    space.render()
    
def terminate(t):
    return t > 4

def setUp():
    workbench.setUp()

def tearDown(e):
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
