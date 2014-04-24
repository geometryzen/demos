from units import *
import numpy as np
from browser import window
from math import *

def f(x):
    return x * x

graph = window.JXG.JSXGraph

b = graph.initBoard("box", {"boundingbox":[-1,1,1,-1],"axis":True,"showCopyright":False})

print meter

print 5 * meter

domainX = np.linspace(0.0, 1.0, 10)
domainX = domainX * meter
print "Are we still alive?"
print domainX.shape
print domainX
rangeY = map(f, domainX)
print rangeY

dataX = map(lambda x: x.quantity, domainX)
dataY = map(lambda x: x.quantity, rangeY)

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
