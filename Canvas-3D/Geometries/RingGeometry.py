from three import *
from browser import *
from workbench import *

THREE = window.THREE

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 10.0

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

geom = THREE.RingGeometry(1,5,32)

mesh = Mesh(geom, MeshBasicMaterial({'color': 0xffff00, 'side': THREE.DoubleSide}))
scene.add(mesh)

movement = 0.02 * VectorE3(1.0, 1.0, 1.0)

workbench = Workbench3D(renderer.domElement, renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)

def terminate(t):
    return t > 15

def tearDown(e):
    workbench.tearDown()
    if e:
        print e
    
WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
