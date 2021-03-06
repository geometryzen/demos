var popUp: Window = open("", "", "width=800, height=600");

var css = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />';
popUp.document.documentElement.innerHTML = css+'<div id="box" class="jxgbox" style="width:800px; height:600px;"></div>'
popUp.document.title = "Parametric Equations";
popUp.document.body.style.backgroundColor = "CCCCCC";
popUp.document.body.style.overflow = "hidden";
var div = popUp.document.getElementById("box");

div.style.width  = "760px";
div.style.height = "560px";

var colorA = '#0000FF';
var colorB = '#FF0000';
var colorC = '#00FF00';
var colorX = '#000000';

var o  = new blade.Euclidean2(0,0,0,0);
var e1 = new blade.Euclidean2(0,1,0,0);
var e2 = new blade.Euclidean2(0,0,1,0);
var a = 2 * e1;
var b = e2;
var c = 2 * e1 + e2;

var board = JXG.JSXGraph.initBoard("box", {boundingbox:[-2, 6, 14, -3], axis:true, grid:true, keepaspectratio: true, showCopyright:false, showNavigation:true, document: popUp.document});

var alpha = board.create('slider', [[10, -1], [12, -1], [0, 1, 4]]);
alpha.setAttribute({strokeColor: colorA});
var beta = board.create('slider', [[10, -2], [12, -2], [0, 1, 4]]);
beta.setAttribute({strokeColor: colorB});

function createInputArrow(mv: blade.Euclidean2, pos: blade.Euclidean2, color: string, handler: (tail:JXG.Point, head:JXG.Point)=>void) {
  var head = board.create('point', [pos.x + mv.x/2, pos.y + mv.y/2], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
  var tail = board.create('point', [function(){return pos.x - mv.x/2;}, function(){return pos.y-mv.y/2;}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
  tail.hideElement();
  board.create('arrow', [tail, head]).setAttribute({strokeColor: color});
  head.on('drag',function(){handler(tail, head)});
}

function createOutputArrow(mv: ()=>blade.Euclidean2, pos: ()=>blade.Euclidean2, color: string) {
    var head = board.create('point', [function(){return mv().x+pos().x;},function(){return mv().y+pos().y;}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
    var tail = board.create('point', [function(){return pos().x;},function(){return pos().y;}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
    head.hideElement();
    tail.hideElement();
    board.create('arrow', [tail, head]).setAttribute({strokeColor: color});
}

createInputArrow(a, 2 * e1 - 2 * e2, colorA, function(tail, head) {a.x=head.X()-tail.X();a.y=head.Y()-tail.Y()});
createInputArrow(b, 5 * e1 - 2 * e2, colorB, function(tail, head) {b.x=head.X()-tail.X();b.y=head.Y()-tail.Y()});
createInputArrow(c, 8 * e1 - 2 * e2, colorC, function(tail, head) {c.x=head.X()-tail.X();c.y=head.Y()-tail.Y()});

createOutputArrow(function(){return a;}, function(){return c;}, colorA);
createOutputArrow(function(){return b;}, function(){return c;}, colorB);
createOutputArrow(function(){return c;}, function(){return o;}, colorC);
createOutputArrow(function(){return c + alpha.Value() * a + beta.Value() * b;},function(){return o;},colorX);