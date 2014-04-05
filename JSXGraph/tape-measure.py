from browser import document, window
from jxg import require

# WARNING: This method for acquiring the library is subject to change,
#          but the API will otherwise stay the same.
graph = require('JXG').JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", {"boundingbox":[-1,3,3,-1],"axis":True})

print board.hasMouseUp
print board.zoomX
print board.xmlString

p1 = board.create('point', [0,0])
p2 = board.create('point', [1,1])
p3 = board.create('point', [2,1])
tape = board.create('tapemeasure', [[0, 2], [2, 2]], {"name":'dist'})

board.zoomX = 2.0
print board.zoomX
print board.origin.x