from browser import *
from workbench import *
from math import *
from units import *
from easel import *

popup = window.open("","","width=800,height=600")
popup.document.body.style.backgroundColor = "202020"
popup.document.body.style.overflow = "hidden"
popup.document.title = "Visualizing Geometric Algebra with WebGL"

canvas2D = glwin.document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D, popup)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text(popup.document.title + ". Hit Esc key to exit.", font, "white")
output.x = 100
output.y = 60
space2D.addChild(output)

stats = window.Stats()
stats.setMode(0)
stats.domElement.style.position = 'absolute'
stats.domElement.style.left = '0px'
stats.domElement.style.top = '0px'
popup.document.body.appendChild(stats.domElement)

def setUp():
    workbench2D.setUp()

def tick(t):
    stats.begin()
    space2D.render()
    stats.end()

def terminate(t):
    return False

def tearDown(e):
    popup.close()
    if e:
        print "Error during animation: %s" % (e)
    else:
        print "Goodbye!"
    workbench2D.tearDown()

runner = windowAnimationRunner(tick, terminate, setUp, tearDown, popup)
