var graph = JXG.JSXGraph;
var sin = Math.sin;

var popUp: Window = open("", "", "width=800, height=600");

//popUp.document.body.style.backgroundColor = "202020";
popUp.document.body.style.overflow = "hidden";
popUp.document.documentElement.innerHTML = '<div id="box" class="jxgbox"></div>'
popUp.document.title = "JXG.Curve";
var div = popUp.document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

var board = graph.initBoard("box", {axis:true, grid:true, showCopyright:false, document:popUp.document})

// Parametric curve
// Create a curve of the form (t-sin(t), 1-cos(t), i.e.
// the cycloid curve.
var curve = board.create('curve', [function(t){ return t-Math.sin(t);}, function(t){ return 1-Math.cos(t);}, 0, 2*Math.PI]);