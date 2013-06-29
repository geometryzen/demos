# experimental/axes.py
# Warning: This is currently slow. It requires optimization in the Python cross-compiler.
# It probably also makes sense to consider convenience functions to do this.
from eight import *
from browser import *
from math import pi, sin, cos, sqrt

COLOR_X_AXIS = 0xff0000
COLOR_Y_AXIS = 0x00ff00
COLOR_Z_AXIS = 0x0000ff
COLOR_GRID = 0x66A1D2
MATERIAL_GRID_MAJOR = LineBasicMaterial({"color": COLOR_GRID,"opacity":0.20,"transparent":True})
MATERIAL_GRID_MINOR = LineBasicMaterial({"color": COLOR_GRID,"opacity":0.02,"transparent":True})

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

def addMainGrid(scene, size):
    sceneObject = Object3D()
    for x in range(-size, size+1):
        if (x != 0):
            gridLineGeometry = Geometry()
            gridLineGeometry.vertices.append(Vector3(x, -size, 0))
            gridLineGeometry.vertices.append(Vector3(x, size, 0))
            material = MATERIAL_GRID_MAJOR if (x % 10 == 0) else MATERIAL_GRID_MINOR
            line = Line(gridLineGeometry, material)
            sceneObject.add(line)
    for y in range(-size, size+1):
        if (y != 0):
            gridLineGeometry = Geometry()
            gridLineGeometry.vertices.append(Vector3(-size, y, 0))
            gridLineGeometry.vertices.append(Vector3(size, y, 0))
            material = MATERIAL_GRID_MAJOR if (y % 10 == 0) else MATERIAL_GRID_MINOR
            line = Line(gridLineGeometry, material)
            sceneObject.add(line)
    scene.add(sceneObject)

def addFadingGrid(scene, size, boundary):
    sceneObject = Object3D()
    for x in range(-size-boundary, size+boundary+1):
        for y in range(-size-boundary, size+boundary+1):
            inside = isInsideX(x, size) and isInsideY(y, size)
            if ((x % 10 == 0) and (y % 10 == 0) and (x != 0) and (y != 0) and  not inside):
                addFadingGridTile(x, y, size, sceneObject)
    scene.add(sceneObject)
    
def isInsideX(x, size):
    return (x >= -size) and (x <= size)
    
def isInsideY(y, size):
    return (y >= -size) and (y <= size)

def addFadingGridTile(x, y, size, sceneObject):
    fadingGridLineGeometry = Geometry()
    fadingGridLineGeometry.vertices.append(Vector3(0,0,0))
    fadingGridLineGeometry.vertices.append(Vector3(10,0,0))
    dx = 0
    if (x < -size):
        dx = -size - x
    elif (x > size):
        dx = x - size
    dy = 0
    if (y < -size):
        dy = -size - y
    elif (y > size):
        dy = y - size
    r = sqrt(dx * dx + dy * dy)
    opacity = 1.0 if (r == 0) else 1.0 / (r * 0.9)
    material = LineBasicMaterial({"color": COLOR_GRID, "opacity": opacity, "transparent": True})    
    line = Line(fadingGridLineGeometry, material)
    line.position.x = x - 10 if (x > 0) else x
    line.position.y = y
    sceneObject.add(line)
    line = Line(fadingGridLineGeometry, material)
    line.position.x = x
    line.position.y = y - 10 if (y > 0) else y
    line.rotation.z = 90 * pi / 180
    sceneObject.add(line)
    
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

renderer = WebGLRenderer({"antialias": True})
renderer.autoClear   = True
renderer.gammaInput  = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)
renderer.sortObjects = False

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

addLights(scene)
addAxes(scene)
addMainGrid(scene, 60)
addFadingGrid(scene, 60, 50)

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
