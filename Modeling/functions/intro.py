from units import *
import numpy as np
from browser import window
from math import *

k = 1.0 * newton / meter

def f(x):
    return k * x * x


N = 100

domainX = np.linspace(-1.0 * meter, +1.0 * meter, N)
rangeY = map(f, domainX)

dataX = map(lambda x: x.quantity, domainX)
dataY = map(lambda x: x.quantity, rangeY)

print min(dataX)
print max(dataX)

graph = window.JXG.JSXGraph

b = graph.initBoard("box", {"boundingbox":[min(dataX),1,max(dataX),-1],"axis":True,"showCopyright":False})

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
