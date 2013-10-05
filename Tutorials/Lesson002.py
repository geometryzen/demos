'''
This lesson demonstrates rendering a pre-populated scene (CartesianSpace).
'''
from browser import WindowAnimationRunner
from geometry import CartesianSpace
from workbench import Workbench

# A CartesianSpace is a pre-made scene containing a renderer, camera, and HTML5 canvas element.
scene = CartesianSpace()

# The Workbench class knows how to incorporate the canvas into the Geometry Zen window document.
# It also know how to clean up at the end of the animation and how to respond to resize events.
workbench = Workbench(scene.renderer, scene.camera)

def tick(t):
    scene.render()

def terminate(t):
    done = t > 4
    return done

def setUp():
    # Incorporate the canvas into the Geometry Zen window document.
    workbench.setUp()

def tearDown():
    # Clean up by removing the canvas from the Geometry Zen window document. 
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
