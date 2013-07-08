from eight import *
from browser import *
from math import pi, random, sin
from time import clock

useLargeCanvas = True

mouseX = 0
mouseY = 0
windowHalfX = window.innerWidth / 2
windowHalfY = window.innerHeight / 2
scene = Scene()

geometry = CubeGeometry(100,100,100)
material = MeshNormalMaterial()

group = Object3D()

for i in range(0, 200):
    mesh = Mesh(geometry, material)
    mesh.position.x = random() * 2000 - 1000
    mesh.position.y = random() * 2000 - 1000
    mesh.position.z = random() * 2000 - 1000
    mesh.rotation.x = random() * 2 * pi
    mesh.rotation.y = random() * 2 * pi
    mesh.matrixAutoUpdate = False
    mesh.updateMatrix();
    group.add(mesh)

scene.add(group)

camera  = PerspectiveCamera(60, 1.0, 1, 10000)
camera.position.z = 500

renderer = CanvasRenderer()
renderer.sortObjects = False
renderer.setClearColor(0x080808, 1.0)

def escKey(downFlag):
    terminate()

keyHandlers = {
 27: escKey
}
    
def onDocumentKeyDown(event):
    event.preventDefault()
    keyHandlers[event.keyCode](True)

def onDocumentKeyUp(event):
    event.preventDefault()
    keyHandlers[event.keyCode](False)
    
def onDocumentMouseMove(event):
    global mouseX, mouseY
    mouseX = (event.clientX - windowHalfX) * 10
    mouseY = (event.clientY - windowHalfY) * 10                               

def onWindowResize():
    global windowHalfX, windowHalfY
    if (useLargeCanvas):
        windowHalfX = window.innerWidth / 2
        windowHalfY = window.innerHeight / 2
        camera.aspect = window.innerWidth / window.innerHeight
        camera.updateProjectionMatrix()
        renderer.size = (window.innerWidth, window.innerHeight)
    else:
        container = document.getElementById("canvas-container")
        windowHalfX = container.clientWidth / 2
        windowHalfY = container.clientHeight / 2
        camera.aspect = container.clientWidth / container.clientHeight
        camera.updateProjectionMatrix()
        renderer.setSize(container.clientWidth, container.clientHeight)
    
def discardCanvases():
    for cs in document.getElementsByTagName("canvas"):
        cs.parentNode.removeChild(cs)
        
requestID = None
frameIndex = 0
DURATION_SECONDS = 15
startTime =  None
frameTime = None
endTime = None

def render():
    camera.position.x += (mouseX - camera.position.x) * 0.05
    camera.position.y += (mouseX - camera.position.y) * 0.05
    camera.lookAt(scene.position)
    
#    currentSeconds = clock()
#    group.rotation.x = sin(currentSeconds * 0.7) * 0.5
#    group.rotation.y = sin(currentSeconds * 0.3) * 0.5
#    group.rotation.z = sin(currentSeconds * 0.2) * 0.5

def run():       
    print "Press ESC to terminate."
    print "This program will 'self-terminate' in "+str(DURATION_SECONDS)+" seconds!"
    discardCanvases()
    if (useLargeCanvas):
        document.body.insertBefore(renderer.domElement, document.body.firstChild)
    else:
        container = document.getElementById("canvas-container")
        container.appendChild(renderer.domElement)

    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)
    document.addEventListener("mousemove", onDocumentMouseMove, False)

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()
    window.requestAnimationFrame(frameZero)

def frameZero(timestamp):
    global requestID, startTime, frameTime, endTime
    startTime = timestamp
    frameTime = startTime
    endTime = startTime + DURATION_SECONDS * 1000
    requestID = window.requestAnimationFrame(animate)
    render()
    renderer.render(scene, camera)
    
def animate(timestamp):
    global requestID, frameIndex, frameTime
    frameIndex += 1
    interval = timestamp - frameTime 
    frameTime = timestamp   
    if frameTime < endTime:
        requestID = window.requestAnimationFrame(animate)
        render()
        renderer.render(scene, camera)
    else:
        terminate()
        
def terminate():
    window.cancelAnimationFrame(requestID)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    time = (frameTime-startTime)/1000
    count = frameIndex+1
    if useLargeCanvas:
        discardCanvases()
    print "Done."

run()
