from browser import document, window
from jxg import require
from math import *

JXG = require('JXG')
JSXGraph = JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = JSXGraph.initBoard("box", {"boundingbox":[-10,10,20,-10]},"axis":True)

def foo(x,unk):
    return sin(x)

b.create('functiongraph',[foo,-pi,pi])
