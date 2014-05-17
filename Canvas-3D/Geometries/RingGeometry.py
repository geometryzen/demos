from three import *
from browser import *
from workbench import *

e1 = VectorE3(1.0, 0.0, 0.0)

space = CartesianSpace()

radiusTop = 1
radiusBottom = 1
height = 5
radialSegments = 32
heightSegments = 5
openEnded = False
geom = RingGeometry(1,5,32)

mesh = Mesh(geom, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1}))
space.add(mesh)

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(t):
    space.render()

def terminate(t):
    return t > 3

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
