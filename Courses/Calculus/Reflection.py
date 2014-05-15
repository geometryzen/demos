from browser import *
from three import *
from workbench import *
from geometry import *

timeOut = 60

space3D = CartesianSpace()
i = VectorE3(1.0, 0.0, 0.0)
j = VectorE3(0.0, 1.0, 0.0)
k = VectorE3(0.0, 0.0, 1.0)
I = i * j * k

v = -j + k
n = 3 * k
r = n * v * n / (n * n)

workbench3D = Workbench3D(space3D.renderer.domElement, space3D.renderer, space3D.camera)

# Probe to show the initial vector.
probeV = ProbeBuilderE3().color(0xFF0000).build()
probeV.quantity = v
space3D.add(probeV.grade1)

# Probe to show the reflecting vector.
probeN = ProbeBuilderE3().color(0x0000FF).build()
probeN.quantity = n
space3D.add(probeN.grade1)

# Probe to show the reflected vector.
probeR = ProbeBuilderE3().color(0xFF00FF).build()
probeR.quantity = r
space3D.add(probeR.grade1)

dt = 0.02

def escKey(event, downFlag):
    event.preventDefault()
    global timeOut
    timeOut = 0

keyHandlers = {
 27: escKey
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except:
        pass

def setUp():
    workbench3D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(t):
    probeV.position = VectorE3(0.0, 0.0, 0.0)
    
    space3D.render()

def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()