from three import *
from browser import *
from workbench import *
from math import pi

timeOut = 5

space = CartesianSpace()

radius = 4.0
radiusCone = 0.32
radiusShaft = 0.02
lengthCone = 0.36
lengthShaft = 0.8
arrowSegments = 8
radialSegments = 32

vortex = VortexGeometry(radius, radiusCone, radiusShaft, lengthCone, lengthShaft, arrowSegments, radialSegments)
vortex.name = "Maxwell"

print repr(vortex)
print "id:             " + str(vortex.id)
print "name:           " + str(vortex.name)
print "uuid:           " + str(vortex.uuid)
#print "radius:         " + str(torus.radius)
#print "tube:           " + str(torus.tube)
#print "radialSegments: " + str(torus.radialSegments)
#print "tubularSegments:" + str(torus.tubularSegments)
#print "arc:            " + str(torus.arc)
print vortex

mesh = Mesh(vortex, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1}))
space.add(mesh)

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

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
    workbench.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
