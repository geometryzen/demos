from three import *
from browser import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

radius = 1
detail = 0 # Must be an integer: 0,1,2,...

icosa = IcosahedronGeometry(radius, detail)

print repr(icosa)
print "radius:         " + str(icosa.radius)
print "detail:         " + str(icosa.detail)
print icosa

mesh = Mesh(icosa, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 3}))
scene.add(mesh)

progressEnd = 10000

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp();

def tick(elapsed):
    mesh.rotation += movement
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > progressEnd

def tearDown():
    workbench.tearDown();

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
