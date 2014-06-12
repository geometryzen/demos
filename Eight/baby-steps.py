from browser import *
from workbench import *
from math import *
from units import *
#from e3ga import *
from geometry import *
from easel import *

# Eight.JS is the new Three.JS!
eight = window.EIGHT
import three as THREE

glwin = window.open("","","width=800,height=600")
glwin.document.body.style.backgroundColor = "080808"
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

scene = eight.scene()

camera = eight.perspectiveCamera(45, 1.0, 0.1, 10000)

renderer = eight.webGLRenderer()
#renderer.setClearColor(THREE.Color(0x080808), 1.0)

box = eight.mesh(eight.boxGeometry(1,2,3))
scene.add(box)
box.position = eight.vectorE3(0,0,-5)

#CartesianSpace(scene, renderer, camera)
camera.position = eight.vectorE3(10.0, 9.0, 8.0)
#camera.up.set(0,0,1)
#camera.lookAt(scene.position)

workbench3D = Workbench3D(renderer.canvas, renderer, camera, glwin)

tau = 2 * pi
omega = (tau / 20) / second
# A unit bivector rotating from k to i
B = BivectorE3(0.0, 0.0, 1.0)
# Just make sure that we really do have a unit bivector.
B = B / magnitude(B)

def setUp():
    monitor.start()
    workbench2D.setUp()
    workbench3D.setUp()

def tick(t):
#    time = t * second
#    theta = omega * time
    # The rotor is defined to have a minus sign.
#    rotor = exp(-B*theta.quantity/2.0)
    # Unfortunately, we have to use a minus sign to convert the rotor grade 2 components to the quaternion values.
#    arrow.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    
#   box.attitude = rotor

#    vortex.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
#    flat.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
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

runner = eight.windowAnimationRunner(tick, terminate, setUp, tearDown, glwin)

def onContextLoss():
    runner.stop()
    renderer.onContextLoss()
    scene.onContextLoss()

def onContextGain(gl):
    scene.onContextGain(gl)
#   renderer.onContextGain()
    runner.start()

monitor = eight.webGLContextMonitor(renderer.canvas, onContextLoss, onContextGain)

onContextGain(renderer.context)

runner.start()
