# LineBasicMaterial demonstration.
from three import *
from browser import *
from workbench import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100.0

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

material = LineBasicMaterial({"wireframe": True})
material.color = Color(0x00FF00)
material.opacity = 0.5

print repr(material)
print "color:              " + str(material.color)
print "opacity:            " + str(material.opacity)
print str(material)

mesh = Mesh(SphereGeometry(50.0, 32, 24), material)

scene.add(mesh)

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench3D(renderer.domElement, renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)

def terminate(t):
    return t > 6

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()
