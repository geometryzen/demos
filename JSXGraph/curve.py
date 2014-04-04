from browser import document, window
from jxg import require
from math import *

JSXGraph = require('JXG').JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = JSXGraph.initBoard("box", {"boundingbox":[-10,10,20,-10],"axis":True})

p = b.create('point',[1,1])
b.create('functiongraph',[lambda x,unk: p.X() * sin(x)])
