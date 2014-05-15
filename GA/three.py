from browser import *
from workbench import *
from math import *
from units import *
from e3ga import *
from geometry import *

import three as THREE
#THREE = window.THREE

scene = THREE.Scene()

camera = THREE.PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10.0, 9.0, 8.0)
camera.up.set(0,0,1)
camera.lookAt(scene.position)

ambientLight = THREE.AmbientLight(0x111111)
scene.add(ambientLight)

pointLight = THREE.PointLight(0xFFFFFF)
pointLight.position.set(20.0, 20.0, 20.0)
scene.add(pointLight)

directionalLight = THREE.DirectionalLight(0xFFFFFF)
directionalLight.position.set(0.0, 1.0, 0.0)
scene.add(directionalLight)

renderer = THREE.WebGLRenderer()
renderer.setClearColor(THREE.Color(0x080808), 1.0)

def material(color=0x0000FF, opacity=1.0, transparent=False):
    return THREE.MeshLambertMaterial({"color": color,"opacity": opacity,"transparent": transparent})

mesh = THREE.Mesh(THREE.BoxGeometry(5, 0.1, 5), material(0x00FF00, 1.0, False))
mesh.position.set(0, -2, 0)
scene.add(mesh)

arrow = THREE.Mesh(THREE.ArrowGeometry(5.0), material(0xFFFF00, 1.0, False))
scene.add(arrow)

box = THREE.Mesh(THREE.BoxGeometry(1,2,3), material(0xFF0000, 0.25, False))
scene.add(box)
box.position.set(3,-3,3)

vortex = THREE.Mesh(THREE.VortexGeometry(4.0, 0.3, 0.05, 0.05, 0.3, 8, 12), material(0x00FFff, 0.3, False))
scene.add(vortex)

flat = THREE.Mesh(THREE.BoxGeometry(10.0,10.0,0.1), material(0x0000FF, 0.25, True))
scene.add(flat)

CartesianSpace(scene, renderer)

workbench = Workbench3D(renderer.domElement, renderer, camera)

tau = 2 * pi
omega = (tau / 20) / second
B = -BivectorE3(0.0, 0.0, 1.0)

def setUp():
    workbench.setUp()

def tick(t):
    time = t * second
    theta = omega * t
    rotor = exp(B*theta.quantity/2.0)
#    arrow.quaternion.set(rotor.w, rotor.yz, rotor.zx, rotor.xy)
    box.attitude = rotor
    box.quaternion.set(rotor.w, rotor.yz, rotor.zx, rotor.xy)
#    vortex.quaternion.set(rotor.w, rotor.yz, rotor.zx, rotor.xy)
    flat.quaternion.set(rotor.w, rotor.yz, rotor.zx, rotor.xy)
    renderer.render(scene, camera)

def tearDown(e):
    workbench.tearDown()
    if e:
        print "Error during animation: %s" % (e)

WindowAnimationRunner(tick, None, setUp, tearDown).start()
