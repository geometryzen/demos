from three import *
from browser import *
from workbench import *

scene = Scene()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10.0, 10.0, 10.0)
camera.lookAt(scene.position)

# White directional light at half intensity shining from the top.
directionalLight = DirectionalLight(0xFFFFFF)
directionalLight.position.set(0.0, 1.0, 0.0)
scene.add(directionalLight)

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

material = MeshLambertMaterial({"color": 0x0000FF})

mesh = Mesh(BoxGeometry(5, 5, 5), material)

scene.add(mesh)

movement = VectorE3(0.02, 0.02, 0.02)

workbench = Workbench3D(renderer.domElement, renderer, camera)

def setUp():
    workbench.setUp()

def tick(t):
    mesh.rotation += movement
    renderer.render(scene, camera)
    
def terminate(t):
    return t > 6

def tearDown(e):
    workbench.tearDown()
    if e:
        print e
    
WindowAnimationRunner(tick, terminate, setUp, tearDown).start()