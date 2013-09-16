# Under Construction
from three import *
from browser import *
from math import pi

i = Vector3(1,0,0)
j = Vector3(0,1,0)
k = Vector3(0,0,1)

scene = Scene()

camera  = PerspectiveCamera(45, 1.0, 0.1, 1000)
camera.up.set(0, 0, 1)
camera.position.set(3, 3, 3)
camera.lookAt(scene.position)

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

redWire = MeshLambertMaterial({"color":0xFF0000})
grnWire = MeshLambertMaterial({"color":0x00FF00})
bluWire = MeshLambertMaterial({"color":0x0000FF})
yloWire = MeshBasicMaterial({"color":0xFFFF00,"wireframe":True})

redGeom = ArrowGeometry()
grnGeom = ArrowGeometry()
bluGeom = ArrowGeometry()
yloGeom = ArrowGeometry()

redMesh = Mesh(redGeom, redWire)
grnMesh = Mesh(bluGeom, grnWire)
bluMesh = Mesh(grnGeom, bluWire)
yloMesh = Mesh(yloGeom, yloWire)
# lookAt is an alternate way of performing a rotation.
# lookAt aligns the arrow with the specified vector.
# It depends on the position of the arrow.
redMesh.lookAt(Vector3(1,0,0))
grnMesh.lookAt(Vector3(0,1,0))
grnMesh.visible = True
yloMesh.lookAt(Vector3(1,0,0))
yloMesh.position = Vector3(0,1,1)

print "position   => " + str(bluMesh.position)
print "rotation   => " + str(bluMesh.rotation)
print "scale      => " + str(bluMesh.scale)
print "visible    => " + str(bluMesh.visible)

scene.add(redMesh)
scene.add(bluMesh)
scene.add(grnMesh)
scene.add(yloMesh)

pointLight = PointLight(0x888888)
pointLight.position.set(20, 20, 20)
scene.add(pointLight)

directionalLight = DirectionalLight(0x888888)
directionalLight.position.set(0, 1, 0)
scene.add(directionalLight)

progressEnd = 6000

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > progressEnd

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()