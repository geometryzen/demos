'''
Under Construction. Nov 4, 2013 (axis)
'''
from three import *
from geometry import *
from workbench import *
from browser import *

space = CartesianSpace()
timeOut = 3

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

def setUp():
    workbench.setUp()

    material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 2})
    mesh = CylinderBuilder().axis(e3).radius(1).height(4).segments(24).material(material).build()
    geometry = mesh.geometry
    for vertex in geometry.vertices:
        print vertex
    faces = geometry.faces
    for face in faces:
        print face
        for normal in face.vertexNormals:
            print normal
        

    space.add(mesh)

def tick(t):
    space.render()
    
def terminate(t):
    return t > timeOut

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()