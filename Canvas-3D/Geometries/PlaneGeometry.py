from three import *
from browser import *
from workbench import *

space = CartesianSpace()

width = 4
depth = 4
widthSegments = 8
depthSegments = 8
plane = PlaneGeometry(width, depth, widthSegments, depthSegments)

print repr(plane)
print "width:          " + str(plane.width)
print "depth:          " + str(plane.depth)
print "widthSegments:  " + str(plane.widthSegments)
print "heightSegments: " + str(plane.heightSegments)
print plane

mesh = Mesh(plane, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
space.add(mesh)

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(t):  
    space.render()
    
def terminate(t):
    return t > 6

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
