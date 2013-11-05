from three import *
from browser import *
from workbench import *
from math import pi

space = CartesianSpace()

text = TextGeometry("Hello")

print repr(text)
print "id:             " + str(text.id)
print "name:           " + str(text.name)
print "uuid:           " + str(text.uuid)
print text

mesh = Mesh(text, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1}))
space.add(mesh)

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 3

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
