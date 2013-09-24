from browser import *
from three import *
from workbench import *

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

camera = PerspectiveCamera()
camera.position.z = 5

pointLight = PointLight(0xFFFFFF);
pointLight.position = camera.position
scene.add(pointLight)

workbench3D = Workbench(renderer, camera)

side = 4.0
thk = 0.3
s2 = 2 * side - thk
s3 = 2 * side + thk

ball = SphereBuilder().color("green").radius(0.8).build()
ball.mass     = ScalarE3(1.0)
ball.momentum = VectorE3(-0.15, -0.23, +0.27)
scene.add(ball)

#print ball.material
print ball.geometry.uuid

#side = side - thk * 0.5 - ball.size.x / 2

def setUp():
    workbench3D.setUp()

def tick(t):
    renderer.render(scene, camera)

def terminate(t):
    return t > 3

def tearDown():
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
