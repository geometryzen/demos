from three import *
from browser import *

scene = Scene()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10, 10, 10)
camera.lookAt(scene.position)

pointLight = PointLight(0xFFFFFF)
pointLight.position.set(20, 20, 20)
scene.add(pointLight)

renderer = WebGLRenderer({"clearColor":0x088080, "clearAlpha":1})
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
#renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

material = MeshLambertMaterial({"color":0x0000FF})
material.name = "bluecube"

mesh = Mesh(CubeGeometry(5, 5, 5), material)

scene.add(mesh)

movement = Vector3(0.02, 0.02, 0.02)

def discardCanvases():
    for canvas in document.getElementsByTagName("canvas"):
        canvas.parentNode.removeChild(canvas)

def onWindowResize(event):
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)

def setUp():
    print "Hello!"
    print "This demonstration will end in 6 seconds."
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)
    
def tick(elapsed):
    mesh.rotation += movement
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 6000

def tearDown():
    discardCanvases()
    window.removeEventListener("resize", onWindowResize, False)
    print "Goodbye!"

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()