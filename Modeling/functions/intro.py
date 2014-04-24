from units import *
import numpy as np
from browser import window
from math import *

x = 3

def fake(p1):
    pass

k = 1.0

def f(x):
    return k * x * x

print f(2)
print f(3)

graph = window.JXG.JSXGraph

b = graph.initBoard("box", {"boundingbox":[-1,1,1,-1],"axis":True,"showCopyright":False})

domainX = np.linspace(-1.0 * meter, +1.0 * meter, 10)
print type(domainX)
rangeY = map(f, domainX)
print type(rangeY)

dataX = map(lambda x: x.quantity, domainX)
dataY = map(lambda x: x.quantity, rangeY)

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})

print k
