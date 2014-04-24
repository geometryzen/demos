from units import *
import numpy as np
from browser import window
from math import *

def f(x):
    return x * x

graph = window.JXG.JSXGraph

b = graph.initBoard("box", {"boundingbox":[-1,1,1,-1],"axis":True,"showCopyright":False})

domainX = np.linspace(0, 1, 100) * meter
dataX = map(lambda x: x, domainX)
dataY = map(f, dataX)

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
