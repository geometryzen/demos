from units import *
import numpy as np
from browser import window
from math import *

def f(x):
    return x

graph = window.JXG.JSXGraph

b = graph.initBoard("box", {"boundingbox":[-10,10,10,-10],"axis":True,"showCopyright":False})

domainX = linspace(0,5,10)
print domainX
dataX = map(lambda x: x, domainX)
print repr(dataX)
dataY = map(f, dataX)

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
