from browser import document, window
from math import *

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = graph.initBoard("box", {"axis":True,"grid":True})

p = b.create('point',[1,1])
b.create('functiongraph',[lambda x,k: p.X() * sin(x)])
