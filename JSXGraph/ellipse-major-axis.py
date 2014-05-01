from browser import document, window
from math import *

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", {"axis":True,"grid":True})

A = board.create('point',[-1,0])
print type(A)
A.foo = A
B = board.create('point',[1,0])
s = board.create('slider',[[-1,-2],[1,-2],[0,4,10]])
print s.Value()
E = board.create('ellipse',[A,B,lambda : s.Value()])
