from units import *

def y(x):
    return x * x

print y(meter)

from browser import document, window
from math import *

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = graph.initBoard("box", {"boundingbox":[-10,10,20,-10],"axis":True})

dataX = [1,2,3,4,5,6,7,8]
dataY = map(y, dataX)

b.create('curve',[dataX,dataY],{"strokeColor":'black'})
