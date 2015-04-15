var graph = JXG.JSXGraph;
var sin = Math.sin;

var popUp: Window = open("", "", "width=800, height=600");

var css = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />';
popUp.document.documentElement.innerHTML = css+'<div id="box" class="jxgbox" style="width:800px; height:600px;"></div>'
popUp.document.title = "JXG.Curve";
//popUp.document.body.style.backgroundColor = "CCCCCC";
popUp.document.body.style.overflow = "hidden";
var div = popUp.document.getElementById("box");

div.style.width  = "400px";
div.style.height = "400px";

var board = graph.initBoard("box", {axis:true, grid:true, showCopyright:false, document: popUp.document});
var p1 = board.create('point', [-1, 4]);
var p2 = board.create('point', [4, 1]);
var q1 = board.create('point', [-2, -3]);
var q2 = board.create('point', [4,3]);

var li1 = board.create('line', [p1,p2], {strokeColor:'black', lastArrow:true});
var li2 = board.create('line', [q1,q2], {lastArrow:true});

var a1 = board.create('angle', [li1, li2, [5.5, 0], [4, 3]], { radius:1 });
var a2 = board.create('angle', [li1, li2, 1, -1], { radius:2 });
