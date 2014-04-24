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

graph = window.JXG.JSXGraph

b = graph.initBoard("box", 
                    {"boundingbox":[min(dataX),max(dataY),max(dataX),min(dataY)],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
