# Demonstractes using the Python three library to create cartesian axes.
# Convenience objects will be provided for common coordinate systems.
from three import *
# We will control the horizontal. We will control the vertical...
from browser import *
from math import pi, sin, cos

COLOR_X_AXIS = 0xff0000
COLOR_Y_AXIS = 0x00ff00
COLOR_Z_AXIS = 0x0000ff
COLOR_GRID = 0x66A1D2
MATERIAL_GRID_MAJOR = LineBasicMaterial({"color": COLOR_GRID,"opacity":0.20,"transparent":True})
MATERIAL_GRID_MINOR = LineBasicMaterial({"color": COLOR_GRID,"opacity":0.02,"transparent":True})

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
camera  = PerspectiveCamera(30, 1.0, 1, 10000)
camera.position.set(-15, 10, 10)
camera.up.x = 0
camera.up.y = 0
camera.up.z = 1
scene.add(camera)

renderer = WebGLRenderer()
renderer.autoClear   = True
renderer.gammaInput  = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

sphere = SphereGeometry(20, 32, 24)

mesh = Mesh(sphere, MeshPhongMaterial({"color": 0x0000FF, "specular": 0x0000FF, "shininess": 100}))
scene.add(mesh)

addLights(scene)
addAxes(scene)

requestID = None
progress = None
progressEnd = 6000
startTime =  None

lastCameraPosition = Vector3(0,0,0)
distance = 1000
polarAngle = 60 * pi / 180
azimuthAngle = 10 * pi / 180
target = {"distance": 300, "polarAngle": polarAngle, "azimuthAngle": azimuthAngle}
targetScenePosition = Vector3(0,0,0)

def render():
    global distance, polarAngle, azimuthAngle
    azimuthAngle += (target["azimuthAngle"] - azimuthAngle) * 0.2
    polarAngle += (target["polarAngle"] - polarAngle) * 0.3
    dDistance = (target["distance"] - distance) * 0.3
    if (distance + dDistance > 1000):
        target["distance"] = 1000
        distance = 1000
    elif (distance + dDistance < 3):
        target["distance"] = 3
        distance = 3
    else:
        distance += dDistance
    dScenePosition = (targetScenePosition - scene.position) * 0.2
    scene.position = scene.position + dScenePosition
    lastCameraPosition = camera.position.clone()
    camera.position.x = distance * sin(polarAngle) * cos(azimuthAngle)
    camera.position.y = distance * sin(polarAngle) * sin(azimuthAngle)
    camera.position.z = distance * cos(polarAngle)
    camera.position = camera.position + scene.position
    dCameraPosition = camera.position - lastCameraPosition
    if ((dScenePosition.length() > 0.1) or (dCameraPosition.length() > 0.1)):
        camera.lookAt(scene.position)

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
