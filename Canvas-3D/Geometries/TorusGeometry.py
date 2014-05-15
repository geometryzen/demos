from three import *
from browser import *
from workbench import *
from math import pi

space = CartesianSpace()

radius = 2
tube = 0.5
radialSegments = 32
tubularSegments = 24
arc = pi * 2

torus = TorusGeometry(radius, tube, radialSegments, tubularSegments, arc)
torus.name = "coffee-cup"

print repr(torus)
print "id:             " + str(torus.id)
print "name:           " + str(torus.name)
print "uuid:           " + str(torus.uuid)
print "radius:         " + str(torus.radius)
print "tube:           " + str(torus.tube)
print "radialSegments: " + str(torus.radialSegments)
print "tubularSegments:" + str(torus.tubularSegments)
print "arc:            " + str(torus.arc)
print torus

mesh = Mesh(torus, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1}))
space.add(mesh)

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 3

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
