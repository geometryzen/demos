# This requires a new feature in JSXGraph build Nightly on 2014-04-05
from browser import window
from math import *

graph = window.JXG.JSXGraph

plotWin = window.open("","JSXGraph-Window","width=420,height=400")
plotDoc = plotWin.document

plotDoc.body.innerHTML = '<div id="box" class="jxgbox"></div>'

div = plotDoc.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", {"document":plotDoc,"axis":True,"grid":True})


A = board.create('point',[1,1],{"name": 'Alice'})
B = board.create('point',[2,2],{"name":'Bob'})

f = board.create('functiongraph',[lambda x: A.X() * sin(x)])
