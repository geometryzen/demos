from geometry import *
from three import *
from browser import *

space = CartesianSpace()

radius = 3
detail = 0 # Must be an integer: 0,1,2,...

icosa = IcosahedronGeometry(radius, detail)

print repr(icosa)
print "radius:         " + str(icosa.radius)
print "detail:         " + str(icosa.detail)
print icosa

mesh = Mesh(icosa, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2}))
space.add(mesh)

progressEnd = 10000

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp();

def tick(elapsed):
    mesh.rotation += movement
    space.render()
    
def terminate(elapsed):
    return elapsed > progressEnd

def tearDown():
    workbench.tearDown();

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
