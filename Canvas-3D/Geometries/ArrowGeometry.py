'''
Under construction. It may be temporarily broken.
'''
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
material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1})
arrow = ArrowBuilder().scale(length).segments(segments).material(material).build()
arrow.name = 'Foo'

print repr(arrow)
print "uuid:            " + str(arrow.uuid)
print "name:            " + str(arrow.name)
print arrow

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
