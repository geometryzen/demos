from browser import *
from workbench import *
from math import *
from units import *
#from geometry import *
from easel import *
from eight import *

glwin = window.open("","","width=800,height=600")
glwin.document.body.style.backgroundColor = "202020"
glwin.document.body.style.overflow = "hidden"
glwin.document.title = "Visualizing Geometric Algebra with WebGL"

canvas2D = glwin.document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D, glwin)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text(glwin.document.title + ". Hit Esc key to exit.", font, "white")
output.x = 100
output.y = 60
space2D.addChild(output)

scene = scene()

camera = perspectiveCamera(45, 1.0, 0.1, 100)

renderer = webGLRenderer()

box = mesh(boxGeometry())
scene.add(box)
box.position = vectorE3(-1.0,-0.5,-5.0)
prism = mesh(prismGeometry())
scene.add(prism)
prism.position = vectorE3(0.0,0.0,-5.0)

workbench3D = workbench3D(renderer.canvas, renderer, camera, glwin)

tau = 2 * pi
omega = (tau / 20) / second
# A unit bivector rotating from k to i
B = BivectorE3(0.0, 0.0, 1.0)
# Just make sure that we really do have a unit bivector.
B = B / magnitude(B)

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()
    monitor.start()

def tick(t):
    time = t * second
    theta = omega * time

    rotor = exp(-B*theta.quantity/2.0)

    box.attitude = rotor
    prism.attitude = rotor

    renderer.render(scene, camera)
    space2D.render()

def terminate(t):
    return False

def tearDown(e):
    monitor.stop()
    glwin.close()
    if e:
        print "Error during animation: %s" % (e)
    else:
        print "Goodbye!"
    workbench3D.tearDown()
    workbench2D.tearDown()
    scene.tearDown()

runner = windowAnimationRunner(tick, terminate, setUp, tearDown, glwin)

def onContextLoss():
    runner.stop()
    renderer.onContextLoss()
    scene.onContextLoss()

def onContextGain(gl):
    scene.onContextGain(gl)
    renderer.onContextGain(gl)
    runner.start()

monitor = webGLContextMonitor(renderer.canvas, onContextLoss, onContextGain)

onContextGain(renderer.context)
