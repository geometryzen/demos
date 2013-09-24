from browser import *
from three import *
from workbench import *

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

camera = PerspectiveCamera()
camera.position.z = 10

pointLight = PointLight(0xFFFFFF);
pointLight.position = camera.position
scene.add(pointLight)

workbench3D = Workbench(renderer, camera)

side = 4.0
thk = 0.3
s2 = 2 * side - thk
s3 = 2 * side + thk

wallR = CubeBuilder().color("red").build()
wallR.position.x = side
scene.add(wallR)

ball = SphereBuilder().color("green").radius(0.8).build()
ball.mass     = ScalarE3(1.0)
ball.momentum = VectorE3(-0.15, -0.23, +0.27)
scene.add(ball)

side = side - thk * 0.5 - ball.geometry.radius
dt = 0.3

def setUp():
    workbench3D.setUp()

def tick(t):
    ball.position = ball.position + (ball.momentum/ball.mass)*dt
    if ball.position.x <= -side or ball.position.x >= side:
        ball.momentum.x = -ball.momentum.x
    if ball.position.y <= -side or ball.position.y >= side:
        ball.momentum.y = -ball.momentum.y
    if ball.position.z <= -side or ball.position.z >= side:
        ball.momentum.z = -ball.momentum.z

    renderer.render(scene, camera)

def terminate(t):
    return t > 10

def tearDown():
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
