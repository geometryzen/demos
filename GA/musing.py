from browser import *
from workbench import *
from math import *
from units import *
from e3ga import *
from geometry import *
from easel import *

# This works both through the Python DaVinci wrapper as well as using JavaScript dynamic wrapping.
# Provided you don't try to use the attitude property on the mesh together with native THREE.
#import three as THREE
THREE = window.THREE

glwin = window.open("","","width=800,height=600")
# Changing the background color is a bit of a hack until I figure out the padding.
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

#renderer = THREE.CanvasRenderer()
renderer = THREE.WebGLRenderer()
renderer.setClearColor(THREE.Color(0x080808), 1.0)

def material(color=0x0000FF, opacity=1.0, transparent=False):
    return THREE.MeshLambertMaterial({"color": color,"opacity": opacity,"transparent": transparent})

mesh = THREE.Mesh(THREE.BoxGeometry(5, 0.1, 5), material(0x00FF00, 1.0, False))
mesh.position.set(0, -2, 0)
scene.add(mesh)

# ArrowGeometry isn't really a THREE artifact right now.
arrow = THREE.Mesh(THREE.ArrowGeometry(4.0), material(0xFFFF00, 1.0, False))
scene.add(arrow)

box = THREE.Mesh(THREE.BoxGeometry(1,2,3), material(0xFF0000, 0.25, False))
scene.add(box)
box.position.set(3,-3,3)

# VortexGeometry isn't really a THREE artifact right now.
vortex = THREE.Mesh(THREE.VortexGeometry(4.0, 0.32, 0.04, 0.08, 0.3, 8, 12), material(0x00FFff, 0.3, False))
scene.add(vortex)

flat = THREE.Mesh(THREE.BoxGeometry(10.0,10.0,0.1), material(0x0000FF, 0.25, True))
scene.add(flat)

CartesianSpace(scene, renderer, camera)

workbench3D = Workbench3D(renderer.domElement, renderer, camera, glwin)

tau = 2 * pi
omega = (tau / 20) / second
# A unit bivector rotating from k to i
B = BivectorE3(0.0, 0.0, 1.0)
# Just make sure that we really do have a unit bivector.
B = B / magnitude(B)

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()

def tick(t):
    time = t * second
    theta = omega * time
    # The rotor is defined to have a minus sign.
    rotor = exp(-B*theta.quantity/2.0)
    # Unfortunately, we have to use a minus sign to convert the rotor grade 2 components to the quaternion values.
    arrow.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    
    box.attitude = rotor
    box.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)

    vortex.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    flat.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w)
    renderer.render(scene, camera)
    space2D.render()

def tearDown(e):
    workbench3D.tearDown()
    workbench2D.tearDown()
    glwin.close()
    if e:
        print "Error during animation: %s" % (e)
    else:
        print "Goodbye!"

WindowAnimationRunner(tick, None, setUp, tearDown, glwin).start()
