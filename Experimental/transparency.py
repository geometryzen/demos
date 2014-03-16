from three import *
from browser import *
from workbench import *

scene = Scene()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10.0, 9.0, 8.0)
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

for i in range(0,3):
    mesh = Mesh(CubeGeometry(5, 5, 5), MeshLambertMaterial({"color":0x0000FF,"opacity":0.1,"transparent":True}))
    mesh.position = VectorE3(i,0,0)
    scene.add(mesh)
    print i

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    renderer.render(scene, camera)

def terminate(t):
    return t > 60

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
