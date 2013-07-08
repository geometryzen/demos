from eight import *
from browser import *
from math import pi

useLargeCanvas = False

scene = Scene()

geometry = CubeGeometry(100,100,100)
material = MeshNormalMaterial()

group = Object3D()

for i in range(0,200):
    print i

camera  = PerspectiveCamera(60, 1.0, 1, 10000)
camera.position.z = 500

renderer = WebGLRenderer()
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

def onWindowResize():
    if (useLargeCanvas):
        camera.aspect = window.innerWidth / window.innerHeight
        camera.updateProjectionMatrix()
        renderer.size = (window.innerWidth, window.innerHeight)
    else:
        container = document.getElementById("canvas-container")
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

    window.addEventListener("resize", onWindowResize, False)
    onWindowResize()
    window.requestAnimationFrame(frameZero)

def frameZero(timestamp):
    global requestID, startTime, frameTime, endTime
    startTime = timestamp
    frameTime = startTime
    endTime = startTime + DURATION_SECONDS * 1000
    requestID = window.requestAnimationFrame(animate)
    renderer.render(scene, camera)
    
def animate(timestamp):
    global requestID, frameIndex, frameTime
    frameIndex += 1
    interval = timestamp - frameTime 
    frameTime = timestamp   
    if frameTime < endTime:
        requestID = window.requestAnimationFrame(animate)
        renderer.render(scene, camera)
    else:
        terminate()
        
def terminate():
    window.cancelAnimationFrame(requestID)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    time = (frameTime-startTime)/1000
    count = frameIndex+1
    if useLargeCanvas:
        discardCanvases()
    print "Done."

run()
