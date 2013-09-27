'''
This program may not work for you because I am working on it right now!
'''
from browser import *
from three import *
from workbench import *
from geometry import *

timeOut = 60

space3D = CartesianSpace()
i = VectorE3(1,0,0)
j = VectorE3(0,0,1)
k = VectorE3(0,0,1)

workbench3D = Workbench(space3D.renderer, space3D.camera)

particle = SphereBuilder().color(0x0000FF).radius(0.1).build()
particle.position = VectorE3(0, 1, 0)
particle.mass     = ScalarE3(1)
particle.velocity = VectorE3(0, -1, 0)
space3D.add(particle)

wire = CylinderBuilder().radius(0.1).height(100).color(0xFF0000).build()
space3D.add(wire)

probeV = ProbeBuilderE3().color(particle.material.color.getHex()).build()
space3D.add(probeV.grade1)

probeB = ProbeBuilderE3().color(0xFF0000).build()
space3D.add(probeB.grade1)

probeF = ProbeBuilderE3().color(0xFFFF00).build()
space3D.add(probeF.grade1)

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

def wireB(position):
    x = position.x
    y = position.y
    quadrance = x * x + y * y
    return VectorE3(-y/quadrance, x/quadrance, 0)

def constantB(position):
    return VectorE3(1, 0, 0)

def outsideCube(position, size):
    if (abs(particle.position % i) > size):
        return True
    if (abs(particle.position % j) > size):
        return True
    if (abs(particle.position % k) > size):
        return True
    return False

def setUp():
    workbench3D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(t):
    global timeOut
    
    B = wireB(particle.position)
    F = particle.velocity.cross(B)

    speedBefore = particle.velocity.magnitude()
    # Integrate the momentum of the particle.
    particle.velocity = particle.velocity + (F * dt / particle.mass)
    speedAfter = particle.velocity.magnitude()

    # This is a bit of a hack to compensate for innacuracy in the simulation.
    # It's only going to work for magnetic fields but we could split momentum change contributions for electric fields.
    particle.velocity = particle.velocity * speedBefore / speedAfter

    # Integrate the position of the particle.    
    particle.position += particle.velocity * dt
    
    probeV.quantity = particle.velocity
    probeV.grade1.position = particle.position

    probeB.quantity = B
    probeB.grade1.position = particle.position

    probeF.quantity = F
    probeF.grade1.position = particle.position
    
    if outsideCube(particle.position, 5):
        timeOut = 0

    # Track the particle with the camera.        
    space3D.camera.position.z = particle.position.z
    space3D.camera.lookAt(particle.position)
    
    space3D.render()

def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
