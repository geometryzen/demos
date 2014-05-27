from easel import *
from three import *
from browser import *
from workbench import *
from geometry import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)

blades = [ScalarE3(1), e1, e2, e3, e1 ^ e2, e2 ^ e3, e3 ^ e1, e1 ^ e2 ^ e3, e1 ^ e3 ^ e2]
binops = ["+", "-", "*", "<<", "^", ">>"]
indexA = 1
indexB = 5
indexOp = 2

timeOut = 600

space3D = CartesianSpace()
canvas3D = space3D.renderer.domElement
workbench3D = Workbench3D(canvas3D, space3D.renderer, space3D.camera)
space3D.camera.position = 3.0 * (1.5 * e1 + 1.0 * e2 + 1.1 * e3).normalize()
space3D.camera.lookAt(VectorE3(0,0,0))
   
canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

colorA = "#7014CC" # Purple Heart
colorB = "#19FF65" # Spring Green
colorC = "#FF9900" # Orange Peel
#colorA = "#FF0000" # "#7014CC" # Purple Heart
#colorB = "#00FF00" # "#19FF65" # Spring Green
#colorC = "#0000FF" # "#FF9900" # Orange Peel
colorP = "#999999" # Light Gray
wireframe = False

font = "20px Helvetica"

rowI = 60
rowC = 90
rowS = 120
rowR = 150

output = Text("Click squares to change operator and operands. Hit Esc key to exit.", font, "white")
output.x = 100
output.y = rowI
space2D.addChild(output)

buttonA = space2D.addChild(Shape())
buttonA.graphics.beginFill(colorA).drawRect(0, 0, 20, 20).endFill()
buttonA.x = 100
buttonA.y = rowS

buttonB = space2D.addChild(Shape())
buttonB.graphics.beginFill(colorB).drawRect(0, 0, 20, 20).endFill()
buttonB.x = 300
buttonB.y = rowS

outputA = Text("", font, colorA)
outputA.x = 100
outputA.y = rowC
space2D.addChild(outputA)

outputA2 = Text("", font, colorA)
outputA2.x = 100
outputA2.y = rowR
space2D.addChild(outputA2)

buttonOp = space2D.addChild(Shape())
buttonOp.graphics.beginFill(colorP).drawRect(0, 0, 20, 20).endFill()
buttonOp.x = 200
buttonOp.y = rowS

outputOp = Text("", font, colorP)
outputOp.x = 200
outputOp.y = rowC
space2D.addChild(outputOp)

outputB = Text("", font, colorB)
outputB.x = 300
outputB.y = rowC
space2D.addChild(outputB)

outputB2 = Text("", font, colorB)
outputB2.x = 300
outputB2.y = rowR
space2D.addChild(outputB2)

outputEq = Text("=", font, colorP)
outputEq.x = 400
outputEq.y = rowC
space2D.addChild(outputEq)

outputC = Text("", font, colorC)
outputC.x = 500
outputC.y = rowC
space2D.addChild(outputC)

outputC2 = Text("", font, colorC)
outputC2.x = 500
outputC2.y = rowR
space2D.addChild(outputC2)

probeC = ProbeBuilderE3().wireframe(wireframe).segments(18).color(colorC).build()
space3D.add(probeC.grade0)
space3D.add(probeC.grade1)
space3D.add(probeC.grade2)
space3D.add(probeC.grade3)
probeC.position = 0.0 * (e1 + e2 +e3)

probeA = ProbeBuilderE3().wireframe(wireframe).segments(18).color(colorA).build()
space3D.add(probeA.grade0)
space3D.add(probeA.grade1)
space3D.add(probeA.grade2)
space3D.add(probeA.grade3)
probeA.position = probeC.position

probeB = ProbeBuilderE3().wireframe(wireframe).segments(18).color(colorB).build()
space3D.add(probeB.grade0)
space3D.add(probeB.grade1)
space3D.add(probeB.grade2)
space3D.add(probeB.grade3)
probeB.position = probeC.position

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
