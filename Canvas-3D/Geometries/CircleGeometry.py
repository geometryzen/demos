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

mesh = Mesh(circle, MeshBasicMaterial({"color": 0xFF00FF,"wireframe": True, "wireframeLinewidth": 3}))
scene.add(mesh)

timeOut = 6000
movement = Vector3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    mesh.rotation += movement
    renderer.render(scene, camera)

def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    workbench.tearDown()
    
WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
