from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *

space3D = CartesianSpace()
canvas3D = space3D.renderer.domElement
#canvas3D.style.position = "absolute"
#canvas3D.style.top = "0px"
#canvas3D.style.left = "0px"
workbench3D = Workbench3D(canvas3D, space3D.renderer, space3D.camera)
   
canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

arrow = ArrowBuilder().scale(3).build()

output = Text("Mouse Events Demonstration", "20px Verdana", "white")
output.x = output.y = 10
space2D.addChild(output)

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()

    space3D.add(arrow)

def tick(t):
    space3D.render()
    space2D.update()
    output.text = str(Euclidean3(1,2,3,4,5,6,7,8))

def terminate(t):
    return t > 5

def tearDown():
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
