'''
Under Construction Sep 25, 2013
'''
from three import *
from browser import *
from workbench import *
from math import pi

timeOut = 60

space = CartesianSpace()

radius = 4
radiusCone = 0.08
radiusShaft = 0.01
radialSegments = 32
arrowSegments = 6

vortex = VortexGeometry(radius, radiusCone, radiusShaft, radialSegments, arrowSegments)
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
