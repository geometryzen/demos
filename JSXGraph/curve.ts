var graph = JXG.JSXGraph;
var sin = Math.sin;

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
var div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

var board = graph.initBoard("box", {axis:true,grid:true, showCopyright:false})

var A = board.create('point',[1,1],{name: 'Alice'})
var B = board.create('point',[2,2],{name:'Bob'})

var f = board.create('functiongraph',[function(x) {return A.X() * sin(x)}])
