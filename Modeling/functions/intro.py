from units import *
from browser import window
from math import *

def f(x):
    return x


graph = window.JXG.JSXGraph

b = graph.initBoard("box", {"boundingbox":[-10,10,10,-10],"axis":True,"showCopyright":False})

dataX = [1,2,3,4,5,6,7,8,9]
dataY = map(f, dataX)

b.create('curve',[dataX,dataY],{"strokeColor":'blue'})
