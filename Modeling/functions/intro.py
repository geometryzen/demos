from e3ga import *
from units import *
from numpy import *
from browser import *
from math import *

# Spring Constant.
k = 20.0 * newton / meter
x0 = 0.0 * meter

# Compute the energy for a given extension.
def f(x):
    return k * (x - x0) ** 2

# How many points to plot.
N = 100

# The domain is the extension values.
extensions = linspace(-1.0 * meter, +1.0 * meter, N)

# The range is the energy.
energies = map(f, extensions)

# Extract quantity from measure data so that it is suitable for JSXGraph.
dataX = map(lambda x: x.quantity, extensions)
dataY = map(lambda x: x.quantity, energies)

minX = min(dataX)
maxX = max(dataX)
minY = min(dataY)
maxY = max(dataY)
rangeX = abs(maxX-minX)
rangeY = abs(maxY-minY)

win = window.open("","GraphWindow","width=720,height=720")

link = win.document.createElement("link")
link.rel  = "stylesheet"
link.href = "http://fonts.googleapis.com/css?family=Open+Sans:400italic,600italic,400,600"
link.type = "text/css"
win.document.head.appendChild(link)

link = win.document.createElement("link")
link.rel  = "stylesheet"
link.href = "http://www.geometryzen.org/css/app.css?version=0.9.215"
link.type = "text/css"
link.media = "all"
win.document.head.appendChild(link)

win.document.title = "Energy vesus Extension for a Spring"

win.document.body.innerHTML = '<div id="box" class="jxgbox"></div>'

div = win.document.getElementById("box")

div.style.width  = "700px"
div.style.height = "700px"

# Compute the bounding box for the graph so that the graph scales automagically.
def boundingBox(padding):
    return [minX-padding*rangeX,
            maxY+padding*rangeY,
            maxX+padding*rangeX,
            minY-padding*rangeY]

box = boundingBox(0.10)

JXG = window.JXG
graph = JXG.JSXGraph

b = graph.initBoard("box", 
                    {"document": win.document,
                     "boundingbox": box,
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
b.create('text',[(maxX+minX)/2, (minY+box[3])/2, 'Extension/( %s )' % meter.uom], {"fontSize":15,"anchorX":'middle',"anchorY":'middle'})
b.create('text',[minX, (maxY+minY)/2, 'Energy/( %s )' % f(meter).uom], {"fontSize":15, "display":'internal', "rotate":90,"anchorX":'middle',"anchorY":'middle'})
b.create('text',[(maxX+minX)/2, maxY, 'Energy versus Extension for a Spring with stiffness k=%s' % k], {"fontSize":15,"anchorX":'middle',"anchorY":'middle'})

# The following is only really needed if you want to incorporate some animation.
# I'm using it here to close the window after a timeout or Esc key press.
def tick(time):
    pass

def terminate(time):
    return False

def setUp():
    pass

def tearDown(e):
    win.close()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, win).start()
