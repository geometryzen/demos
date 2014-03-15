from three import *
from browser import *
from workbench import *

scene = Scene()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10.0, 10.0, 10.0)
camera.lookAt(scene.position)

ambientLight = AmbientLight(0x111111)
scene.add(ambientLight)

pointLight = PointLight(0xFFFFFF)
pointLight.position.set(20.0, 20.0, 20.0)
scene.add(pointLight)

directionalLight = DirectionalLight(0xFFFFFF)
directionalLight.position.set(0.0, 1.0, 0.0)
scene.add(directionalLight)

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0xCCCCCC), 1.0)

material = MeshLambertMaterial({"color":0x0000FF})
material.name = "bluecube"
material.opacity = 0.1

print "repr(material) => " + repr(material)
print "id: " + str(material.id)
print "name: " + material.name
print "color: " + str(material.color)
print "needsUpdate: " + str(material.needsUpdate)
print "opacity: " + str(material.opacity)
print "overdraw: " + str(material.overdraw)
print "transparent: " + str(material.transparent)
print "visible: " + str(material.visible)
print "str(material) => " + str(material)

mesh = Mesh(CubeGeometry(5, 5, 5), material)

scene.add(mesh)

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)

def terminate(t):
    return t > 6

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
