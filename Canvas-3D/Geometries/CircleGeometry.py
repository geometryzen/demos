from three import *
from browser import *
from math import pi

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

radius = 50
segments = 32
thetaStart = 0
thetaLength = 2 * pi
circle = CircleGeometry(radius, segments, thetaStart, thetaLength)

print repr(circle)
print "radius:          " + str(circle.radius)
#print "height:         " + str(cube.height)
#print "depth:          " + str(cube.depth)
#print "widthSegments:  " + str(cube.widthSegments)
#print "heightSegments: " + str(cube.heightSegments)
#print "depthSegments:  " + str(cube.depthSegments)
print circle

mesh = Mesh(circle, MeshBasicMaterial({"wireframe": True, "wireframeLinewidth": 3}))
scene.add(mesh)

movement = 0.02 * Vector3(1, 1, 1)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    mesh.rotation += movement
    renderer.render(scene, camera)

def terminate(elapsed):
    return elapsed > 6000

def tearDown():
    workbench.tearDown()
    
WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
