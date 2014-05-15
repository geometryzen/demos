import three as THREE
from browser import *
from workbench import *
from math import pi
from e3ga import *

i = VectorE3(1.0, 0.0, 0.0)
j = VectorE3(0.0, 1.0, 0.0)
k = VectorE3(0.0, 0.0, 1.0)

scene = THREE.Scene()

camera  = THREE.PerspectiveCamera(45, 1.0, 0.1, 1000)
camera.up.set(0.0, 0.0, 1.0)
camera.position.set(3.0, 3.0, 3.0)
camera.lookAt(scene.position)

renderer = THREE.WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(THREE.Color(0x080808), 1.0)

redWire = THREE.MeshLambertMaterial({"color":0xFF0000})
grnWire = THREE.MeshLambertMaterial({"color":0x00FF00})
bluWire = THREE.MeshLambertMaterial({"color":0x0000FF})
yloWire = THREE.MeshBasicMaterial({"color":0xFFFF00,"wireframe":True})

redGeom = THREE.ArrowGeometry()
grnGeom = THREE.ArrowGeometry(1.0)
bluGeom = THREE.ArrowGeometry(0.5)
yloGeom = THREE.ArrowGeometry(0.5)

redMesh = THREE.Mesh(redGeom, redWire)
grnMesh = THREE.Mesh(grnGeom, grnWire)
bluMesh = THREE.Mesh(bluGeom, bluWire)
yloMesh = THREE.Mesh(yloGeom, yloWire)
# lookAt is an alternate way of performing a rotation.
# lookAt aligns the arrow with the specified vector.
# It depends on the position of the arrow.
redMesh.lookAt(VectorE3(1.0, 0.0, 0.0))
grnMesh.lookAt(VectorE3(0.0, 1.0, 0.0))
grnMesh.visible = True
yloMesh.lookAt(VectorE3(1.0, 0.0, 0.0))
yloMesh.position = VectorE3(0.0, 1.0, 1.0)

print "position   => " + str(bluMesh.position)
print "rotation   => " + str(bluMesh.rotation)
print "scale      => " + str(bluMesh.scale)
print "visible    => " + str(bluMesh.visible)

scene.add(redMesh)
scene.add(bluMesh)
scene.add(grnMesh)
scene.add(yloMesh)

pointLight = THREE.PointLight(0x888888)
pointLight.position.set(20.0, 20.0, 20.0)
scene.add(pointLight)

directionalLight = THREE.DirectionalLight(0x888888)
directionalLight.position.set(0.0, 1.0, 0.0)
scene.add(directionalLight)

progressEnd = 6

workbench = Workbench3D(renderer.domElement, renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    renderer.render(scene, camera)
    
def terminate(t):
    return t > progressEnd

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()