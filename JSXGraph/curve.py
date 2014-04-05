from browser import document, window
from math import *

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", {"axis":True,"grid":True})

A = board.create('point',[1,1],{"name": 'Alice'})
B = board.create('point',[2,2],{"name":'Bob'})

def foo(x):
    print x
    return A.X() * sin(x)

f = board.create('functiongraph',[foo])
