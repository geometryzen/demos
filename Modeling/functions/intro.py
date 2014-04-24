from units import *
import numpy as np
from browser import window
from math import *

# Spring Constant.
k = 1.0 * newton / meter
x0 = 0.25 * meter

# Compute the energy for a given extension.
def f(x):
    return k * (x - x0) ** 2

# How many points to plot.
N = 100

# The domain is the extension values.
extensions = np.linspace(-1.0 * meter, +1.0 * meter, N)

# The range is the energy.
energies = map(f, extensions)

# Convert data so that it is suitable for JSXGraph.
dataX = map(lambda x: x.quantity, extensions)
dataY = map(lambda x: x.quantity, energies)

JXG = window.JXG
graph = JXG.JSXGraph

rangeX = abs(max(dataX)-min(dataX))
rangeY = abs(max(dataY)-min(dataY))

b = graph.initBoard("box", 
                    {"boundingbox":[min(dataX),max(dataY)+0.05*rangeY,max(dataX),min(dataY)],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":True
                     })

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
xLabel = b.create('text',[0.6, 0.05, 'Extension / %s' % meter.uom], {"fontSize":15})
yLabel = b.create('text',[-0.05, 0.8, 'Energy / %s' % f(meter).uom], {"fontSize":15, "display":'internal', "rotate":90})
