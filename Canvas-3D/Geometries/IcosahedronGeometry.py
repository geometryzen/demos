from geometry import *
from three import *
from browser import *
from workbench import *

space = CartesianSpace()

radius = 3
detail = 0 # Must be an integer: 0,1,2,...

geom = IcosahedronGeometry(radius, detail)

mesh = Mesh(icosa, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2}))

space.add(mesh)

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

def setUp():
    workbench.setUp();

def tick(t):
    mesh.rotation += movement
    space.render()
    
def terminate(t):
    return t > 5

def tearDown(e):
    workbench.tearDown();
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()
