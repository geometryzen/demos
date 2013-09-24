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

ball = SphereBuilder().color("green").radius(0.8).build()
ball.mass = 1.0
print ball.mass
scene.add(ball)

def setUp():
    workbench3D.setUp()
    print "setUp"

def tick(t):
    renderer.render(scene, camera)

def terminate(t):
    return t > 3

def tearDown():
    print "tearDown"
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
