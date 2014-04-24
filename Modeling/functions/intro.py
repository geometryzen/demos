from units import *
import numpy as np
from browser import window
from math import *

x = 3

def fake(p1):
    pass

k = 1.0 * newton / meter

def makeFunction(s):
    def f(x,y):
        return s * x * x
    return f

print makeFunction(k)(2,1)
print makeFunction(k)(3)

graph = window.JXG.JSXGraph

b = graph.initBoard("box", {"boundingbox":[-1,1,1,-1],"axis":True,"showCopyright":False})

domainX = np.linspace(-1.0 * meter, +1.0 * meter, 10)
print type(domainX)
rangeY = map(makeFunction(k), domainX)
print type(rangeY)

dataX = map(lambda x: x.quantity, domainX)
dataY = map(lambda x: x.quantity, rangeY)

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})

print k
