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
domainX = np.linspace(-1.0 * meter, +1.0 * meter, N)

# The range is the energy.
rangeY = map(f, domainX)

# Convert data so that it is suitable for JSXGraph.
dataX = map(lambda x: x.quantity, domainX)
dataY = map(lambda x: x.quantity, rangeY)

JXG = window.JXG
JXG.Options.text.display = 'internal'
graph = JXG.JSXGraph

b = graph.initBoard("box", 
                    {"boundingbox":[min(dataX),max(dataY),max(dataX),min(dataY)],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
xLabel = b.create('text',[0.7,0.05, 'Extension / %s' % meter.uom], {})
yLabel = b.create('text',[0.0,1.0, 'Energy / %s' % f(meter).uom], {})

tRot = b.create('transform', [30.0*pi/180.0, -2,-1], {"type":'rotate'}) 
tRot.bindTo(yLabel)
b.update()
