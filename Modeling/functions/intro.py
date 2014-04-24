from units import *
import numpy as np
from browser import window
from math import *


def f(x):
    k = 1.0
    return k * x * x

graph = window.JXG.JSXGraph

b = graph.initBoard("box", {"boundingbox":[-1,1,1,-1],"axis":True,"showCopyright":False})

domainX = np.linspace(-1.0 * meter, +1.0 * meter, 100)

rangeY = map(f, domainX)

dataX = map(lambda x: x.quantity, domainX)
dataY = map(lambda x: x.quantity, rangeY)

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
