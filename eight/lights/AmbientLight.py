from eight import *
from browser import *

for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(10, 10, 10)
camera.lookAt(scene.position)

ambientLight = AmbientLight(0xFFFFFF)
scene.add(ambientLight)

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

material = MeshLambertMaterial({"color":0x0000FF})
material.name = "bluecube"

print "repr(material) => " + repr(material)
print "id: " + str(material.id)
print "name: " + material.name
print "color: " + str(material.color)
print "needsUpdate: " + str(material.needsUpdate)
print "opacity: " + str(material.opacity)
print "overdraw: " + str(material.overdraw)
print "transparent: " + str(material.transparent)
print "visible: " + str(material.visible)
print "str(material) => " + str(material)

mesh = Mesh(CubeGeometry(5, 5, 5), material)

scene.add(mesh)

requestID = None
progress = None
progressEnd = 6000
startTime = None
movement = Vector3(0.02, 0.02, 0.02)

def render():
    mesh.rotation.add(movement)
        
    renderer.render(scene, camera)

def onWindowResize():
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)
    
def animate(timestamp):
    global requestID, progress, startTime
    if (startTime):
        progress = timestamp - startTime
    else:
        if (timestamp):
            startTime = timestamp
        else:
            progress = 0
        
    if (progress < progressEnd):
        requestID = window.requestAnimationFrame(animate)
        render()
    else:
        window.cancelAnimationFrame(requestID)
        # container.removeChild(renderer.domElement)

window.addEventListener("resize", onWindowResize, False)

onWindowResize()

animate(None)