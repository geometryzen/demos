from e3ga import *
from three import *
from browser import *
from math import pi,sqrt

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)

for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

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

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

redWire = MeshLambertMaterial({"color":0xFF0000})
grnWire = MeshLambertMaterial({"color":0x00FF00})
bluWire = MeshLambertMaterial({"color":0x0000FF})
yloWire = MeshBasicMaterial({"color":0xFFFF00,"wireframe":True, "wireframeLinewidth":2})

redGeom = ArrowGeometry()
grnGeom = ArrowGeometry()
bluGeom = ArrowGeometry()
quarters = 2
yloGeom = CircleGeometry(1, 8 * quarters, 0, pi*quarters/2)

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
yloMesh.useQuaternion = True
a = k # from vector
b = (k + j) / sqrt(2)
R = (1 + b * a)/(a + b).length()
print "R => " + repr(R)
yloMesh.quaternion.set(-R.yz, -R.zx, -R.xy, R.w)

print "position   => " + str(bluMesh.position)
print "quaternion => " + str(bluMesh.quaternion)
print "rotation   => " + str(bluMesh.rotation)
print "eulerOrder => " + str(bluMesh.eulerOrder)
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

def setUp():
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tick(elapsed):
    renderer.render(scene, camera)

def terminate(elapsed):
    return elapsed > 6000

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    for canvas in document.getElementsByTagName("canvas"):
        canvas.parentNode.removeChild(canvas)

def onWindowResize(event):
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
