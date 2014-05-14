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

material = MeshLambertMaterial({"color":0x0000FF,"opacity":0.5,"transparent":True})
material.name = "bluecube"

mesh = Mesh(CubeGeometry(5, 5, 1), material)

scene.add(mesh)

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench3D(renderer.domElement, renderer, camera)

timeOut = 3

def setUp():
    workbench.setUp()

def tick(t):
    renderer.render(scene, camera)

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, None, setUp, tearDown).start()