from three import *
from browser import *
from workbench import *
from math import pi

scene = Scene()

# Aspect ratio will be reset in onWindowResize
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 200

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

radius = 100
tube = 40
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

mesh = Mesh(torus, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 10

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
