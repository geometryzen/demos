from units import *
import numpy as np
from browser import window
from math import *

# Spring Constant.
k = 1.0 * newton / meter
x0 = 2.0 * meter

# Compute the energy for a given extension.
def f(x):
    return k * (x - x0) ** 2

# How many points to plot.
N = 100

# The domain is the extension values.
extensions = np.linspace(-1.0 * meter, +1.0 * meter, N)

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

JXG = window.JXG
graph = JXG.JSXGraph

# Compute the bounding box for the graph so that the graph scales automagically.
def boundingBox(padding):
    return [minX-padding*rangeX,
            maxY+padding*rangeY,
            maxX+padding*rangeX,
            minY-padding*rangeY]

box = boundingBox(0.10)

b = graph.initBoard("box", 
                    {"boundingbox": box,
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
xLabel = b.create('text',[(maxX+minX)/2, (minY+box[3])/2, 'Extension / %s' % meter.uom], {"fontSize":15,"anchorX":'middle',"anchorY":'middle'})
yLabel = b.create('text',[minX, (maxY+minY)/2, 'Energy / %s' % f(meter).uom], {"fontSize":15, "display":'internal', "rotate":90,"anchorX":'middle',"anchorY":'middle'})
title = b.create('text',[(maxX+minX)/2, maxY, 'Energy versus Extension for a Spring'], {"fontSize":15,"anchorX":'middle',"anchorY":'middle'})
