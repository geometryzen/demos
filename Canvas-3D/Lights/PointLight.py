from three import *
from browser import *
from workbench import *

scene = Scene()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10, 10, 10)
camera.lookAt(scene.position)

pointLight = PointLight(0xFFFFFF, 1, 100)
pointLight.position.set(20, 20, 20)
scene.add(pointLight)

renderer = WebGLRenderer()
renderer.setClearColor(Color(0xCCCCCC), 1.0)

mesh = Mesh(CubeGeometry(5, 5, 5), MeshLambertMaterial({"color":0x0000FF}))

scene.add(mesh)

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    print "Hello!"
    print "This demonstration will end in 6 seconds."
    workbench.setUp()
    
def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 6

def tearDown():
    workbench.tearDown()
    print "Goodbye!"

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()