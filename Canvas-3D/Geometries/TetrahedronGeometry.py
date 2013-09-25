from three import *
from browser import *
from workbench import *

scene = Scene()

# Aspect ratio will be reset in onWindowResize
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

radius = 1
detail = 0 # Must be an integer: 0,1,2,...

tetra = TetrahedronGeometry(radius, detail)

print repr(tetra)
print "radius:         " + str(tetra.radius)
print "detail:         " + str(tetra.detail)
print tetra

mesh = Mesh(tetra, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(elapsed):   
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 6

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
