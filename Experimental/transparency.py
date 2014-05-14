from three import *
from browser import *
from workbench import *
from math import *
from units import *

scene = Scene()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10.0, 9.0, 8.0)
camera.up.set(0,0,1)
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

def material(color, opacity, transparent):
    return MeshLambertMaterial({"color": color,"opacity": opacity,"transparent": transparent})

#for i in range(3,7):
#    mesh = Mesh(CubeGeometry(5, 0.1, 5), material(0x0000FF, 0.25, True))
#    mesh.position = VectorE3(0, i-5,0)
#    scene.add(mesh)

rotor = exp(-BivectorE3(0.0, 1.0, 0.0)*pi/4.0)
shape = CylinderBuilder().scale(5).attitude(rotor).material(material(0xFFFF00, 1.0, False)).build()
scene.add(shape)

space = CartesianSpace(scene, renderer)

workbench = Workbench3D(renderer.domElement, renderer, camera)

omega = 0.2 / second

def setUp():
    workbench.setUp()

def tick(t):
    time = t * second
    theta = omega * t
    shape.attitude = rotor
    renderer.render(scene, camera)

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, None, setUp, tearDown).start()
