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

def material(color=0x0000FF, opacity=1.0, transparent=False):
    return MeshLambertMaterial({"color": color,"opacity": opacity,"transparent": transparent})

mesh = Mesh(CubeGeometry(5, 0.1, 5), material(0x00FF00, 1.0, False))
mesh.position = VectorE3(0, -2, 0)
scene.add(mesh)

arrow = Mesh(ArrowGeometry(5.0, None, 24), material(0xFFFF00, 1.0, False))
scene.add(arrow)

cube = Mesh(CubeGeometry(1,2,3), material(0xFF0000, 0.25, False))
scene.add(cube)

vortex = Mesh(VortexGeometry(4.0, 0.3, 0.05, 0.05, 0.3, 8, 12), material(0x00FFff, 0.3, False))
scene.add(vortex)

flat = Mesh(CubeGeometry(10.0,10.0,0.1), material(0x0000FF, 0.25, True))
scene.add(flat)

#CartesianSpace(scene, renderer)

workbench = Workbench3D(renderer.domElement, renderer, camera)

tau = 2 * pi
omega = (tau / 20) / second
B = -BivectorE3(0.0, 0.0, 1.0)
e1 = VectorE3(0,0,1)
cube.position = VectorE3(3,-3,3)

def setUp():
    workbench.setUp()

def tick(t):
    time = t * second
    theta = omega * t
    rotor = exp(B*theta.quantity/2.0)
    arrow.attitude = rotor
    cube.attitude = rotor
    vortex.attitude = rotor
    flat.attitude = rotor
    renderer.render(scene, camera)

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, None, setUp, tearDown).start()
