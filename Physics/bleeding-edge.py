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

workbench3D = Workbench3D(space3D.renderer.domElement, space3D.renderer, space3D.camera)

particle = SphereBuilder().color("blue").radius(0.1).build()
particle.charge   = ScalarE3(1.0)
particle.mass     = ScalarE3(1.0)
particle.position = VectorE3(0.0, 1.0, 0.0)
particle.velocity = VectorE3(0.0, -1.0, 0.0)
space3D.add(particle)

wire = CylinderBuilder().radius(0.1).height(2).color("blue").build()
space3D.add(wire)

# Probe to show the velocity of the particle.
probeV = ProbeBuilderE3().color(particle.material.color.getHex()).build()
space3D.add(probeV.grade1)

# Probe to show the magnetic field at the particle position.
probeB = ProbeBuilderE3().color(0xFF0000).build()
space3D.add(probeB.grade1)
space3D.add(probeB.grade2)

# Probe to show the Lorentz force on the charged particle.
probeF = ProbeBuilderE3().color(0xFFFF00).build()
space3D.add(probeF.grade1)

dt = 0.02

def wireB(position):
    x = position.x
    y = position.y
    quadrance = x * x + y * y
    # Convert the traditional magnetic field to a bivector.
    return -I * VectorE3(-y/quadrance, x/quadrance, 0.0)

def outsideCube(position, size):
    if (abs(particle.position | i) > size):
        return True
    if (abs(particle.position | j) > size):
        return True
    if (abs(particle.position | k) > size):
        return True
    return False

def setUp():
    workbench3D.setUp()

def tick(t):
    global timeOut
    
    B = wireB(particle.position)
    F = particle.charge * (particle.velocity << B)

    speedBefore = particle.velocity.magnitude()
    # Integrate the momentum of the particle.
    particle.velocity += (F * dt / particle.mass)
    speedAfter = particle.velocity.magnitude()

    # This is a bit of a hack to compensate for innacuracy in the simulation.
    # It's only going to work for magnetic fields but we could split momentum change contributions for electric fields.
    particle.velocity *= speedBefore / speedAfter

    # Integrate the position of the particle.    
    particle.position += particle.velocity * dt
    
    probeV.quantity = particle.velocity
    probeV.position = particle.position

    probeB.quantity = B
    probeB.position = particle.position

    probeF.quantity = F
    probeF.position = particle.position
    
    if outsideCube(particle.position, 5):
        timeOut = 0

    # Track the particle with the camera.        
    space3D.camera.position.z = particle.position.z
    space3D.camera.lookAt(particle.position)
    
    space3D.render()

def terminate(t):
    return t > timeOut

def tearDown(e):
    workbench3D.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
