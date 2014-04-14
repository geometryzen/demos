from browser import document, window
from math import *

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box"></div>'
div = document.getElementById("box")

div.style.width  = "600px"
div.style.height = "600px"

board = graph.initBoard("box",{"grid":True})

board.create('axis', [[0,0], [1,0]], {"withLabel": True, "name": "abc", "label": {"offset": [35,50]}});
