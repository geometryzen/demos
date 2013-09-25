from three import *
from browser import *
from workbench import *

space = CartesianSpace()

radius = 1
detail = 0 # Must be an integer: 0,1,2,...

tetra = TetrahedronGeometry(radius, detail)

print repr(tetra)
print "radius:         " + str(tetra.radius)
print "detail:         " + str(tetra.detail)
print tetra

mesh = Mesh(tetra, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 3}))
space.add(mesh)

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(elapsed):   
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 6

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
