from three import *
from browser import *
from workbench import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 20.0

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

material = MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 3})
mesh = Mesh(cube, material)
#mesh = CubeBuilder().width(width).height(height).depth(depth).material(material).build()
scene.add(mesh)

timeOut = 6
movement = 0.02 * VectorE3(1.0, 1.0, 1.0)

workbench = Workbench3D(renderer.domElement, renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)
    
def terminate(t):
    return t > timeOut

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()