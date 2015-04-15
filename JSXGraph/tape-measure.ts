var graph = JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
var div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

var board = graph.initBoard("box", {"boundingbox":[-1,3,3,-1],"axis":true})

var p1 = board.create('point', [0,0])
var p2 = board.create('point', [1,1])
var p3 = board.create('point', [2,1])
var tape = board.create('tapemeasure', [[0, 2], [2, 2]], {"name":'distance'})