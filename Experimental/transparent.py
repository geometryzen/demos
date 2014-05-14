from three import *
from browser import *
from workbench import *
from math import *

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

material = MeshLambertMaterial({"color":0x0000FF,"opacity":0.5,"transparent":True})
mesh = Mesh(CubeGeometry(5, 5, 1), material)
scene.add(mesh)

e3 = VectorE3(0,0,1)

rotor = exp(-BivectorE3(0.0, 1.0, 0.0)*pi/4.0)
shape = ArrowBuilder().scale(2).wireframe(False).color(0x0000FF).axis(e3).segments(12).material(MeshLambertMaterial({"color":0x0000FF,"opacity":0.5,"transparent":True})).build()
scene.add(shape)

workbench = Workbench3D(renderer.domElement, renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    renderer.render(scene, camera)

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, None, setUp, tearDown).start()