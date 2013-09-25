from three import *
from browser import *
from workbench import *

space = CartesianSpace()

# All arguments are optional and the defaults, in order, are as follows.
length = 8
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

material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2})
mesh = Mesh(arrow, material)
space.add(mesh)

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    space.render()
    
def terminate(t):
    return t > 6

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
