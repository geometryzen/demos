from three import *
from browser import *
from workbench import *

space = CartesianSpace()

width = 4.0
depth = 4.0
widthSegments = 3
depthSegments = 2
plane = PlaneGeometry(width, depth, widthSegments, depthSegments)

print repr(plane)
print "width:         " + str(plane.width)
print "depth:         " + str(plane.depth)
print plane

mesh = Mesh(plane, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2}))
space.add(mesh)

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(t):  
    space.render()
    
def terminate(t):
    return t > 4

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
