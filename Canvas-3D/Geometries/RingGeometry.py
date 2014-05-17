from three import *
from browser import *
from workbench import *
from math import pi

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100.0

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

geom = CircleGeometry(radius, segments, thetaStart, thetaLength)

mesh = Mesh(geom, MeshBasicMaterial({"wireframe": True, "wireframeLinewidth": 3}))
scene.add(mesh)

movement = 0.02 * VectorE3(1.0, 1.0, 1.0)

workbench = Workbench3D(renderer.domElement, renderer, camera)

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
