'''
This lesson demonstrates adding a keyboard handler.
We respond to the Escape key in order to end the animation prematurely.
'''
from browser import document, WindowAnimationRunner
from geometry import CartesianSpace, SphereBuilder
from math import cos, sin, pi
from workbench import Workbench3D

T = 5
omega = 2 * pi / T
R = 4

space = CartesianSpace()

sphere = SphereBuilder().color(0x0000FF).radius(0.2).build()
space.add(sphere)

workbench = Workbench3D(space.renderer.domElement, space.renderer, space.camera)

timeOut = 10

def tick(t):
    sphere.position.set(R * cos(omega*t), R * sin(omega*t), 0)
    space.render()

def terminate(time):
    # The animation ends when the time is greater than the timeOut.
    # The animation may be ended prematurely by changing the timeOut value.
    done = time > timeOut
    return done

def setUp():
    workbench.setUp()
    # Finally, start listening for keyboard events.
    document.addEventListener("keydown", onDocumentKeyDown, False)

def tearDown():
    # Firstly, stop listening for keyboard events.
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench.tearDown()

# This function performs the required action for the Escape keyboard event.   
def escKey(event, downFlag):
    event.preventDefault()
    global timeOut
    timeOut = 0

# This variable maps keyboard codes to functions.
keyHandlers = {
 27: escKey
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except:
        pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
