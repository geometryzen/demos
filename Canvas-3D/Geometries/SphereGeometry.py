from three import *
from browser import *
from workbench import *
from math import pi

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

radius = 50
widthSegments = 32
heightSegments = 24
phiStart = 0
phiLength = 2 * pi
thetaStart = 0
thetaLength = pi
sphere = SphereGeometry(radius, widthSegments, heightSegments, phiStart, phiLength, thetaStart, thetaLength)

print repr(sphere)
print "radius:         " + str(sphere.radius)
print "widthSegments:  " + str(sphere.widthSegments)
print "heightSegments: " + str(sphere.heightSegments)
print "phiStart:       " + str(sphere.phiStart)
print "phiLength:      " + str(sphere.phiLength)
print "thetaStart:     " + str(sphere.thetaStart)
print "thetaLength:    " + str(sphere.thetaLength)
print sphere

mesh = Mesh(sphere, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement    
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 6

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
