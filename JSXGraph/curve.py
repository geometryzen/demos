from browser import document, window
from jxg import require
from math import sin

JXG = require('JXG')
JSXGraph = JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = JSXGraph.initBoard("box", {"boundingbox":[-10,10,20,-10]})

b.create('functiongraph',[lambda x: sin(x)])
