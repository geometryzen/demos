from three import *
from browser import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 20

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

width = 10
height = 10
depth = 10
widthSegments = 1
heightSegments = 2
depthSegments = 3
cube = CubeGeometry(width, height, depth, widthSegments, heightSegments, depthSegments)

print repr(cube)
print "width:          " + str(cube.width)
print "height:         " + str(cube.height)
print "depth:          " + str(cube.depth)
print "widthSegments:  " + str(cube.widthSegments)
print "heightSegments: " + str(cube.heightSegments)
print "depthSegments:  " + str(cube.depthSegments)
print cube

mesh = Mesh(cube, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

timeOut = 6000
movement = 0.02 * Vector3(1, 1, 1)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    mesh.rotation += movement
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()