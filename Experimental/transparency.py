from thr ee import *
from browser import *
from workbench import *

scene = Scene()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10.0, 9.0, 8.0)
camera.lookAt(scene.position)

ambientLight = AmbientLight(0x111111)
scene.add(ambientLight)

pointLight = PointLight(0xFFFFFF)
pointLight.position.set(20.0, 20.0, 20.0)
scene.add(pointLight)

directionalLight = DirectionalLight(0xFFFFFF)
directionalLight.position.set(0.0, 1.0, 0.0)
scene.add(directionalLight)

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

for i in range(0,10):
    mesh = Mesh(CubeGeometry(0.1, 5, 5), MeshLambertMaterial({"color": 0x0000FF,"opacity": 0.25,"transparent": True}))
    mesh.position = VectorE3(i-5,0,0)
    scene.add(mesh)
    
    mesh = Mesh(CubeGeometry(5, 0.1, 5), MeshLambertMaterial({"color": 0x00FF00,"opacity": 0.25,"transparent": True}))
    mesh.position = VectorE3(0, i-5,0)
    scene.add(mesh)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    renderer.render(scene, camera)

#def terminate(t):
#    return t > 60

def tearDown(e):
    workbench.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, None, setUp, tearDown).start()
