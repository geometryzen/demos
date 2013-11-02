from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *
from math import exp, pi

blades = [ScalarE3(1), e1, e2, e3, e1 ^ e2, e2 ^ e3, e3 ^ e1, e1 ^ e2 ^ e3]
binops = ["+", "-", "*", "<<", "^", ">>"]
indexA = 1
indexB = 2
indexOp = 0

timeOut = 600

space3D = CartesianSpace()
canvas3D = space3D.renderer.domElement
workbench3D = Workbench3D(canvas3D, space3D.renderer, space3D.camera)
space3D.camera.position = 1.5 * (e1 + e2 + e3)
space3D.camera.lookAt(VectorE3(0,0,0))
   
canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

output = Text("Click squares to change blades. Hit Esc key to exit.", "16px Helvetica", "white")
output.x = 100
output.y = 60
space2D.addChild(output)

buttonA = space2D.addChild(Shape())
buttonA.graphics.beginFill("red").drawRect(0, 0, 20, 20).endFill()
buttonA.x = 100
buttonA.y = 100

buttonB = space2D.addChild(Shape())
buttonB.graphics.beginFill("green").drawRect(0, 0, 20, 20).endFill()
buttonB.x = 300
buttonB.y = 100

outputA = Text("", "20px Helvetica", "red")
outputA.x = 100
outputA.y = 120
space2D.addChild(outputA)

outputA2 = Text("", "20px Helvetica", "red")
outputA2.x = 100
outputA2.y = 140
space2D.addChild(outputA2)

buttonOp = space2D.addChild(Shape())
buttonOp.graphics.beginFill("gray").drawRect(0, 0, 20, 20).endFill()
buttonOp.x = 200
buttonOp.y = 100

outputOp = Text("*", "20px Helvetica", "white")
outputOp.x = 200
outputOp.y = 120
space2D.addChild(outputOp)

outputB = Text("", "20px Helvetica", "green")
outputB.x = 300
outputB.y = 120
space2D.addChild(outputB)

outputB2 = Text("", "20px Helvetica", "green")
outputB2.x = 300
outputB2.y = 140
space2D.addChild(outputB2)

outputEq = Text("=", "20px Helvetica", "white")
outputEq.x = 400
outputEq.y = 120
space2D.addChild(outputEq)

outputC = Text("", "20px Helvetica", "blue")
outputC.x = 500
outputC.y = 120
space2D.addChild(outputC)

outputC2 = Text("", "20px Helvetica", "blue")
outputC2.x = 500
outputC2.y = 140
space2D.addChild(outputC2)

probeC  = ProbeBuilderE3().wireframe(True).segments(12).color(0xFF9900).build()
space3D.add(probeC.grade0)
space3D.add(probeC.grade1)
space3D.add(probeC.grade2)
space3D.add(probeC.grade3)

probeA  = ProbeBuilderE3().wireframe(True).segments(12).color(0xCCCCCC).build()
space3D.add(probeA.grade0)
space3D.add(probeA.grade1)
space3D.add(probeA.grade2)
space3D.add(probeA.grade3)

probeB  = ProbeBuilderE3().wireframe(True).segments(18).color(0x00FF00).build()
space3D.add(probeB.grade0)
space3D.add(probeB.grade1)
space3D.add(probeB.grade2)
space3D.add(probeB.grade3)

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
    
def onClickA(event):
    global indexA
    indexA = (indexA + 1) % len(blades)

def onClickB(event):
    global indexB
    indexB = (indexB + 1) % len(blades)

def onClickOp(event):
    global indexOp
    indexOp = (indexOp + 1) % len(binops)

def setUp():
    workbench2D.setUp()
    workbench3D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    buttonA.addEventListener("click", onClickA)
    buttonB.addEventListener("click", onClickB)
    buttonOp.addEventListener("click", onClickOp)

def tick(t):
    A = blades[indexA]
    B = blades[indexB]
    if binops[indexOp] == "+":
        C = A + B
    elif binops[indexOp] == "-":
        C = A - B
    elif binops[indexOp] == "*":
        C = A * B
    elif binops[indexOp] == "<<":
        C = A << B
    elif binops[indexOp] == "^":
        C = A ^ B
    elif binops[indexOp] == ">>":
        C = A >> B
    elif binops[indexOp] == "m":
        C = A % B
    else:
        C = ScalarE3(0)
    outputA.text = str(A)
    outputA2.text = repr(A)
    outputB.text = str(B)
    outputB2.text = repr(B)
    outputC.text = str(C)
    outputC2.text = repr(C)
    outputOp.text = str(binops[indexOp])
    try:
        probeA.quantity = A
        probeB.quantity = B
        probeC.quantity = C
        space3D.render()
        space2D.render()
    except:
        pass

def terminate(t):
    return t > timeOut

def tearDown():
    buttonA.removeEventListener("click", onClickA)
    buttonB.removeEventListener("click", onClickB)
    buttonOp.removeEventListener("click", onClickOp)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench3D.tearDown()
    workbench2D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()

