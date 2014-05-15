from three import *
from browser import *
from workbench import *
from math import pi

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100.0

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

radius = 50
segments = 32
thetaStart = 0
thetaLength = 2 * pi
circle = CircleGeometry(radius, segments, thetaStart, thetaLength)
circle.name = "Foo"

print repr(circle)
print "uuid:            " + str(circle.uuid)
print "name:            " + str(circle.name)
print circle

mesh = Mesh(circle, MeshBasicMaterial({"wireframe": True, "wireframeLinewidth": 3}))
scene.add(mesh)

movement = 0.02 * VectorE3(1.0, 1.0, 1.0)

workbench = Workbench3D(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)

def terminate(t):
    return t > 3

def tearDown(e):
    workbench.tearDown()
    if e:
        print e
    
WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
