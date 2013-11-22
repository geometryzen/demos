from three import *
from browser import *
from workbench import *

e1 = VectorE3(1.0, 0.0, 0.0)

space = CartesianSpace()

radiusTop = 1
radiusBottom = 1
height = 5
radialSegments = 32
heightSegments = 5
openEnded = False
cylinder = CylinderGeometry(radiusTop, radiusBottom, height, radialSegments, heightSegments, openEnded, e1)

print repr(cylinder)
print "radiusTop:      " + str(cylinder.radiusTop)
print "radiusBottom:   " + str(cylinder.radiusBottom)
print "height:         " + str(cylinder.height)
print "radialSegments: " + str(cylinder.radialSegments)
print "heightSegments: " + str(cylinder.heightSegments)
print "openEnded:      " + str(cylinder.openEnded)

mesh = Mesh(cylinder, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1}))
space.add(mesh)

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(t):
    space.render()

def terminate(t):
    return t > 3

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
