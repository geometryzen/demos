from units import *
from numpy import *
from browser import window
from math import *

def f(x):
    return x

graph = window.JXG.JSXGraph

b = graph.initBoard("box", {"boundingbox":[-10,10,10,-10],"axis":True,"showCopyright":False})

dataX = linspace(-5,5,100)
dataY = map(f, dataX)

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
