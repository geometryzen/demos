# cartesian-axes.py
from three import *
# We will control the horizontal. We will control the vertical...
from browser import *
from math import pi

COLOR_X_AXIS = 0xff0000
COLOR_Y_AXIS = 0x00ff00
COLOR_Z_AXIS = 0x0000ff

def addAxes(scene):
    axes = [Geometry(),Geometry(),Geometry(),Geometry(),Geometry(),Geometry()]
    axes[0].vertices.append(Vector3(0,0,0))
    axes[0].vertices.append(Vector3(1000,0,0))
    
    axes[1].vertices.append(Vector3(0,0,0))
    axes[1].vertices.append(Vector3(0,1000,0))
    
    axes[2].vertices.append(Vector3(0,0,0))
    axes[2].vertices.append(Vector3(0,0,1000))
    
    axes[3].vertices.append(Vector3(0,0,0))
    axes[3].vertices.append(Vector3(-1000,0,0))
    
    axes[4].vertices.append(Vector3(0,0,0))
    axes[4].vertices.append(Vector3(0,-1000,0))
    
    axes[5].vertices.append(Vector3(0,0,0))
    axes[5].vertices.append(Vector3(0,0,-1000))
    
    sceneObject = Object3D()
    sceneObject.add(Line(axes[0], LineBasicMaterial({"color":COLOR_X_AXIS, "opacity":0.5,"transparent":True})))
    sceneObject.add(Line(axes[1], LineBasicMaterial({"color":COLOR_Y_AXIS, "opacity":0.5,"transparent":True})))
    sceneObject.add(Line(axes[2], LineBasicMaterial({"color":COLOR_Z_AXIS, "opacity":0.5,"transparent":True})))
    sceneObject.add(Line(axes[3], LineBasicMaterial({"color":COLOR_X_AXIS, "opacity":0.2,"transparent":True})))
    sceneObject.add(Line(axes[4], LineBasicMaterial({"color":COLOR_Y_AXIS, "opacity":0.2,"transparent":True})))
    sceneObject.add(Line(axes[5], LineBasicMaterial({"color":COLOR_Z_AXIS, "opacity":0.2,"transparent":True})))
    
    return scene.add(sceneObject)

def addLights(scene):
    pointLight = PointLight(0xFFFFFF)
    pointLight.position.set(100, 100, 100)
    scene.add(pointLight)
    pointLight = PointLight(0xFFFFFF)
    pointLight.position.set(100, -100, 100)
    scene.add(pointLight)
    pointLight = PointLight(0xFFFFFF)
    pointLight.position.set(100, 100, -100)
    scene.add(pointLight)
    pointLight = PointLight(0xFFFFFF)
    pointLight.position.set(100, -100, -100)
    scene.add(pointLight)

# Discard the old canvas if it exists. 
for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

# Aspect ratio will be reset in onWindowResize
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

renderer = WebGLRenderer()
renderer.autoClear   = True
renderer.gammaInput  = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

sphere = SphereGeometry(50, 32, 24)

mesh = Mesh(sphere, MeshPhongMaterial({"color": 0xFF0000, "specular": 0xFF0000, "shininess": 100}))
scene.add(mesh)

addLights(scene)
addAxes(scene)

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
