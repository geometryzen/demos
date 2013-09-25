from three import *
from browser import *
from workbench import *
from math import pi

space = CartesianSpace()

radius = 2
tube = 0.5
radialSegments = 32
tubularSegments = 24
arc = 2.0 * pi

torus = TorusGeometry(radius, tube, radialSegments, tubularSegments, arc)

print repr(torus)
print "radius:         " + str(torus.radius)
print "tube:           " + str(torus.tube)
print "radialSegments: " + str(torus.radialSegments)
print "tubularSegments:" + str(torus.tubularSegments)
print "arc:            " + str(torus.arc)
print torus

mesh = Mesh(torus, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth": 1}))
space.add(mesh)

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 10

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
