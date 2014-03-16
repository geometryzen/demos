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
renderer.setClearColor(Color(0x080808), 1.0)

material = MeshLambertMaterial({"color":0x0000FF,"opacity":0.1,"transparent":True})

mesh = Mesh(CubeGeometry(5, 5, 5), material)
m2 = Mesh(CubeGeometry(5, 5, 5), MeshLambertMaterial({"color":0x0000FF,"opacity":0.1,"transparent":True}))
m3 = Mesh(CubeGeometry(2, 2, 2), MeshLambertMaterial({"color":0x0000FF,"opacity":0.1,"transparent":True}))

scene.add(mesh)
scene.add(m2)
scene.add(m3)

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
