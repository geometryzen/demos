from three import *
from browser import *
from workbench import *

space = CartesianSpace()

# All arguments are optional and the defaults, in order, are as follows.
length = 6
segments = 12
radiusShaft = 0.01
radiusCone = 0.08
lengthCone = 0.2
geometry = ArrowGeometry(1, ScalarE3(1), segments, length, radiusShaft)
material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1})
arrow = Mesh(geometry, material)
#arrow = ArrowBuilder().scale(length).segments(segments).material(material).build()
arrow.geometry.name = 'Foo'

print repr(geometry)
print repr(arrow.geometry)
print "uuid:            " + str(arrow.geometry.uuid)
print "name:            " + str(arrow.geometry.name)
print arrow.geometry

space.add(arrow)

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    space.render()
    
def terminate(t):
    return t > 4

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
