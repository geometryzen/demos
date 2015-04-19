var popUp: Window = open("", "", "width=800, height=600");

var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

var css = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />';
popUp.document.documentElement.innerHTML = css+'<div id="box" class="jxgbox" style="width:800px; height:600px;"></div>'
popUp.document.title = "Reciprocal Basis";
popUp.document.body.style.backgroundColor = "CCCCCC";
popUp.document.body.style.overflow = "hidden";
var div = popUp.document.getElementById("box");

div.style.width  = "760px";
div.style.height = "560px";

var colorA  = '#0000FF';
var colorB  = '#FF0000';

var o  = new blade.Euclidean2(0,0,0,0);
var e1 = new blade.Euclidean2(0,1,0,0);
var e2 = new blade.Euclidean2(0,0,1,0);
var a = 2 * e1;
var b = e2;

// View
var board = JXG.JSXGraph.initBoard("box", {boundingbox:[-2, 3, 6, -3], axis:false, grid:false, keepaspectratio: true, showCopyright:false, showNavigation:true, document: popUp.document});

function createInputArrow(mv: blade.Euclidean2, pos: blade.Euclidean2, color: string, handler: (tail:JXG.Point, head:JXG.Point)=>void, localized: boolean) {
  var denom = localized ? 2 : 1;
  var k = localized ? 1 : 0;
  var head = board.create('point', [pos.x + mv.x/denom, pos.y + mv.y/denom], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
  var tail = board.create('point', [function(){return pos.x - k * mv.x/2;}, function(){return pos.y - k * mv.y/2;}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
  tail.hideElement();
  board.create('arrow', [tail, head]).setAttribute({strokeColor: color});
  head.on('drag',function(){handler(tail, head)});
}

function createOutputArrow(mv: ()=>blade.Euclidean2, pos: ()=>blade.Euclidean2, color: string, dash: number) {
    var head = board.create('point', [function(){return mv().x+pos().x;},function(){return mv().y+pos().y;}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
    var tail = board.create('point', [function(){return pos().x;},function(){return pos().y;}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
    head.hideElement();
    tail.hideElement();
    board.create('arrow', [tail, head]).setAttribute({strokeColor: color, dash:dash});
}

createInputArrow(a, o, colorA, function(tail, head) {a.x=head.X()-tail.X();a.y=head.Y()-tail.Y()}, false);
createInputArrow(b, o, colorB, function(tail, head) {b.x=head.X()-tail.X();b.y=head.Y()-tail.Y()}, false);

createOutputArrow(
  function() {
    var I = a ^ b;
    var m = I | I;
    var inverse = I / m;
    return b * inverse;
    
  }, function(){return o;}, colorA,3);
createOutputArrow(
  function() {
    var I = a ^ b;
    var m = I | I;
    var inverse = I / m;
    return -a * inverse;
    
  }, function(){return o;}, colorB,3);
