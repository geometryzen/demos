from browser import *
from three import *
from workbench import *
from random import random
from math import *

e1 = VectorE3(1.0, 0.0, 0.0)
e2 = VectorE3(0.0, 1.0, 0.0)
e3 = VectorE3(0.0, 0.0, 1.0)

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

camera = PerspectiveCamera()
camera.position.z = 15

pointLight = PointLight(0xFFFFFF);
pointLight.position = camera.position
scene.add(pointLight)

workbench3D = Workbench(renderer, camera)

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

ball = SphereBuilder().color("green").radius(0.4).build()
# This could equally well be done by using the velocity as the variable to describe the motion.
ball.mass     = ScalarE3(1.0)
ball.momentum = 1.0 * VectorE3(-0.15, -0.23, +0.27)
scene.add(ball)

side = side - thk * 0.5 - ball.geometry.radius
dt = 0.3

frames = 0.0
elapsed = 0.0
timeout = 6.0

def setUp():
    workbench3D.setUp()

def tick(t):
    global frames, elapsed
    frames += 1.0
    elapsed = t
    ball.position += (ball.momentum / ball.mass) * dt
    # Use a scalar product to project the ball position.
    # Use a geometric vector sandwich to compute the reflection.
    if abs(ball.position % e1) >= side:
        ball.momentum = - e1 * ball.momentum * e1
    if abs(ball.position % e2) >= side:
        ball.momentum = - e2 * ball.momentum * e2
    if abs(ball.position % e3) >= side:
        ball.momentum = - e3 * ball.momentum * e3
    renderer.render(scene, camera)

def terminate(t):
    return t > timeout

def tearDown(e):
    workbench3D.tearDown()
    print "frames per second: %d" % (frames / elapsed)
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
