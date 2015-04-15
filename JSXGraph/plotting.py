from browser import document, window
from math import *

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" /><div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = graph.initBoard("box", {"boundingbox":[-10,10,20,-10],"axis":True})

p = b.create('point',[1,4])
dataX = [1,2,3,4,5,6,7,8]
dataY = [0.3,4.0,-1,2.3,7,9,8,9]

b.create('curve',[dataX,dataY],{"strokeColor":'red'})
b.create('curve',[dataX,lambda x,unused: p.X()*sin(x)*x],{"strokeColor":'blue',"dash":1})
