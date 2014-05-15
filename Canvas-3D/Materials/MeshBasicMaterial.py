from three import *
from browser import *
from workbench import *

scene = Scene()

camera = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100.0

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

material = MeshBasicMaterial({"color":0x0000FF, "wireframe":True})
material.wireframeLinewidth = 1
material.name = "greenie"

print "repr(material) => " + repr(material)
print "id: " + str(material.id)
print "uuid: " + material.uuid
print "name: " + material.name
print "color: " + str(material.color)
print "needsUpdate: " + str(material.needsUpdate)
print "opacity: " + str(material.opacity)
print "overdraw: " + str(material.overdraw)
print "transparent: " + str(material.transparent)
print "visible: " + str(material.visible)
print "wireframe: " + str(material.wireframe)
print "wireframeLinewidth: " + str(material.wireframeLinewidth)
print "str(material) => " + str(material)

mesh = Mesh(SphereGeometry(50.0, 32, 24), material)

scene.add(mesh)

workbench = Workbench3D(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation.x = mesh.rotation.x + 0.02
    mesh.rotation.y = mesh.rotation.y + 0.02
    mesh.rotation.z = mesh.rotation.z + 0.02
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 6

def tearDown(e):
    workbench.tearDown()
    print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()
