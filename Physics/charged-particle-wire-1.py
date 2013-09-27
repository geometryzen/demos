from browser import *
from easel import *
from three import *
from workbench import *
from math import pow
from random import random

timeOut = 30

space3D = CartesianSpace()

workbench3D = Workbench(space3D.renderer, space3D.camera)

particle = SphereBuilder().color("blue").radius(0.4).build()
particle.position = VectorE3(0, 1, -5)
particle.mass     = ScalarE3(0.5)
particle.momentum = VectorE3(0, -1, 0) * particle.mass
space3D.add(particle)

dt = 0.05

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

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tick(t):
    velocity = particle.momentum / particle.mass

    F = velocity.cross(wireB(particle.position))
    # Seem to have a problem here that F.v is not close to zero.
    output.text = str(F % velocity)
    particle.momentum = particle.momentum + F * dt
    particle.position = particle.position + (particle.momentum / particle.mass) * dt
    
    
    space3D.render()
    space2D.update()

def terminate(t):
    return t > timeOut

def tearDown():
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
