from three import *
from browser import *
from workbench import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 15

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

width = 16
height = 16
widthSegments = 8
heightSegments = 8
plane = PlaneGeometry(width, height, widthSegments, heightSegments)

print repr(plane)
print "width:          " + str(plane.width)
print "height:         " + str(plane.height)
print "widthSegments:  " + str(plane.widthSegments)
print "heightSegments: " + str(plane.heightSegments)
print plane

mesh = Mesh(plane, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

requestID = None
progress = None
progressEnd = 12000
startTime =  None
movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement    
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 6

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
