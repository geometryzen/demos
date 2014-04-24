from units import *
import numpy as np
from browser import window
from math import *

# Spring Constant.
k = 1.0 * newton / meter
x0 = 0.2 * meter

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

JXG = window.JXG
graph = JXG.JSXGraph

# Compute the bounding box for the graph so that the graph scales automagically.
def boundingBox(xs, ys, padding):
    minX = min(xs)
    maxX = max(xs)
    minY = min(ys)
    maxY = max(ys)
    rangeX = abs(maxX-minX)
    rangeY = abs(maxY-minY)
    return [minX-padding*rangeX,
            maxY+padding*rangeY,
            maxX+padding*rangeX,
            minY-padding*rangeY]

b = graph.initBoard("box", 
                    {"boundingbox": boundingBox(dataX, dataY, 0.10),
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
xLabel = b.create('text',[0.6, 0.05, 'Extension / %s' % meter.uom], {"fontSize":15})
yLabel = b.create('text',[-0.05, 0.8, 'Energy / %s' % f(meter).uom], {"fontSize":15, "display":'internal', "rotate":90})
title = b.create('text',[-0.9, 1.4, 'Energy versus Extension for a Spring'], {"fontSize":15})
