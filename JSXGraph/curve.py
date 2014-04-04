from browser import document, window
import jxg
from math import *

JSXGraph = jxg.require('JXG').JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = JSXGraph.initBoard("box", {"axis":True,"grid":True})

p = b.create('point',[1,1])
b.create('functiongraph',[lambda x: p.X() * sin(x)])
