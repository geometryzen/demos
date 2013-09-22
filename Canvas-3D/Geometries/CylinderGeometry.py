from three import *
from browser import *
from workbench import *

renderer = WebGLRenderer({"antialias": True})
renderer.setClearColor(Color(0x080808), 1.0)

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

radiusTop = 20
radiusBottom = 20
height = 100
radialSegments = 32
heightSegments = 5
openEnded = False
cylinder = CylinderGeometry(radiusTop, radiusBottom, height, radialSegments, heightSegments, openEnded)

print repr(cylinder)
print "radiusTop:      " + str(cylinder.radiusTop)
print "radiusBottom:   " + str(cylinder.radiusBottom)
print "height:         " + str(cylinder.height)
print "radialSegments: " + str(cylinder.radialSegments)
print "heightSegments: " + str(cylinder.heightSegments)
print "openEnded:      " + str(cylinder.openEnded)
try:
    print "bogus:          " + str(cylinder.bogus)
except AttributeError as e:
    print e
print cylinder

try:
    cylinder.bogus = 23
except AttributeError as e:
    print e

mesh = Mesh(cylinder, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 3}))
scene.add(mesh)

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)

def terminate(t):
    return t > 3

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
