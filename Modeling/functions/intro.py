from units import *

def f(x):
    return x

from browser import document, window
from math import *

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = graph.initBoard("box", {"boundingbox":[-10,10,10,-10],"axis":True,"showCopyright":False})

dataX = [1,2,3,4,5,6,7,8]
dataY = map(f, dataX)

b.create('curve',[dataX,dataY],{"strokeColor":'black'})
