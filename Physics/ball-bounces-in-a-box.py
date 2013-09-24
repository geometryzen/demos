from browser import *
from three import *
from workbench import *
from random import random

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

camera = PerspectiveCamera()
camera.position.z = 15

pointLight = PointLight(0xFFFFFF);
pointLight.position = camera.position
scene.add(pointLight)

workbench3D = Workbench(renderer, camera)

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)

side = 4.0
thk = 0.3
s2 = 2 * side - thk
s3 = 2 * side + thk

wallR = CubeBuilder().width(thk).height(s2).depth(s3).color("red").build()
wallR.position.x = +side
wallL = CubeBuilder().width(thk).height(s2).depth(s3).color("red").build()
wallL.position.x = -side
wallB = CubeBuilder().width(s3).height(thk).depth(s3).color("blue").build()
wallB.position.y = -side
wallT = CubeBuilder().width(s3).height(thk).depth(s3).color("blue").build()
wallT.position.y = +side
wallZ = CubeBuilder().width(s2).height(s2).depth(thk).color("gray").build()
wallZ.position.z = -side
scene.add(wallR)
scene.add(wallL)
scene.add(wallB)
scene.add(wallT)
scene.add(wallZ)

ball = SphereBuilder().color("green").radius(0.8).build()
# This could equally well be done by using the velocity as the variable to describe the motion.
ball.mass     = ScalarE3(1.0)
ball.momentum = VectorE3(random(), random(), random())
scene.add(ball)

side = side - thk * 0.5 - ball.geometry.radius
dt = 0.3

def setUp():
    workbench3D.setUp()

def tick(t):
    ball.position += (ball.momentum / ball.mass) * dt
    # Use a scalar product to project the ball position.
    # Use a geometric vector sandwich to compute the reflection. 
    if abs(ball.position % i) >= side:
        ball.momentum = - i * ball.momentum * i

    if abs(ball.position % j) >= side:
        ball.momentum = - j * ball.momentum * j
        
    if abs(ball.position % k) >= side:
        ball.momentum = - k * ball.momentum * k

    renderer.render(scene, camera)

def terminate(t):
    return t > 15

def tearDown():
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
