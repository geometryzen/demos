from browser import document, window
from math import *

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", {"axis":True,"grid":True})

A = board.create('point',[-1,0])
B = board.create('point',[1,0])
C = board.create('point',[0,2])
E = board.create('ellipse',[A,B,C])
