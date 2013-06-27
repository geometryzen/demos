# MeshLambertMaterial.py
from three import *
from browser import *
from math import pi

# Discard the old canvas if it exists. 
for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

camera  = PerspectiveCamera(35, 1.0, 0.1, 10000)
camera.position.set(-15, 10, 10)

light = PointLight(0xFFFFFF)
light.position.set(20, 20, 20)
scene.add(light)

renderer = WebGLRenderer()
renderer.autoClear   = True
renderer.gammaInput  = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

material = MeshLambertMaterial({"color":0x00FF00})
material.name = "greenie"

print "repr(material)    => " + repr(material)
#print "id:                  " + str(material.id)
#print "name:                " + material.name
#print "color:               " + str(material.color)
#print "needsUpdate:         " + str(material.needsUpdate)
#print "opacity:             " + str(material.opacity)
#print "overdraw:            " + str(material.overdraw)
#print "transparent:         " + str(material.transparent)
#print "visible:             " + str(material.visible)
#print "wireframe:           " + str(material.wireframe)
#print "wireframeLinewidth:  " + str(material.wireframeLinewidth)
print "str(material)     => " + str(material)

mesh = Mesh(CubeGeometry(50, 50, 50), material)

scene.add(mesh)

requestID = None
progress = None
progressEnd = 6000
startTime =  None

def render():
    mesh.rotation.x = mesh.rotation.x + 0.02
    mesh.rotation.y = mesh.rotation.y + 0.02
    mesh.rotation.z = mesh.rotation.z + 0.02
        
    renderer.render(scene, camera)

def onWindowResize():
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)
    
def step(timestamp):
    global requestID, progress, startTime
    if (startTime):
        progress = timestamp - startTime
    else:
        if (timestamp):
            startTime = timestamp
        else:
            progress = 0
        
    if (progress < progressEnd):
        requestID = window.requestAnimationFrame(step)
        render()
    else:
        window.cancelAnimationFrame(requestID)
        # container.removeChild(renderer.domElement)
        # TODO: Remove the "resize" event listener

window.addEventListener("resize", onWindowResize, False)

onWindowResize()

step(None)