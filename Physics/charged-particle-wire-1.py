'''
Under construction
'''
from browser import *
from easel import *
from three import *
from workbench import *
from math import pow
from random import random

timeOut = 60

space3D = CartesianSpace()

workbench3D = Workbench(space3D.renderer, space3D.camera)

particle = SphereBuilder().color("yellow").radius(0.1).build()
particle.position = VectorE3(0, 1, 0)
particle.mass     = ScalarE3(1)
particle.velocity = VectorE3(0, -1, 0)
space3D.add(particle)

grade0 = SphereBuilder().wireframe(True).color(0xFFFF00).segments(12).build()
grade1 = ArrowBuilder().color(0x0000FF).segments(32).build()
grade2 = VortexBuilder().color(0x0000FF).build()
grade3 = CubeBuilder().wireframe(True).color(0xFFFF00).segments(1).build()

probeB  = ProbeE3(grade0, grade1, grade2, grade3)
space3D.add(probeB)

dt = 0.02

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

output = Text("", "20px Helvetica", "white")
output.x = window.innerWidth / 2
output.y = window.innerHeight / 2
space2D.addChild(output)

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

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(t):
    B = wireB(particle.position)
    F = particle.velocity.cross(B)

    magnitudeBefore = particle.velocity.magnitude()
    particle.velocity = particle.velocity + (F * dt / particle.mass)
    magnitudeAfter = particle.velocity.magnitude()

    # This is a bit of a hack to compensate for innacuracy in the simulation.
    # It's only going to work for magnetic fields but we could split momentum change contributions for electric fields.
    particle.velocity = particle.velocity * magnitudeBefore / magnitudeAfter
    particle.position += particle.velocity * dt
    
    probeB.quantity = B
    
    space3D.render()
    space2D.update()

def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
