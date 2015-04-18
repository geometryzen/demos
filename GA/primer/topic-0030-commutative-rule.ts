var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

var graph = JXG.JSXGraph;

var popUp: Window = open("", "", "width=800, height=600");

var css = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />';
popUp.document.documentElement.innerHTML = css+'<div id="box" class="jxgbox" style="width:800px; height:600px;"></div>'
popUp.document.title = "Commutative Rule";
popUp.document.body.style.backgroundColor = "CCCCCC";
popUp.document.body.style.overflow = "hidden";
var div = popUp.document.getElementById("box");

div.style.width  = "760px";
div.style.height = "560px";

var board = graph.initBoard("box", {boundingbox:[-1,2,3,-1], axis:false, grid:false, keepaspectratio: true, showCopyright:false, showNavigation:true, document: popUp.document});

// Create an arrow providing two points.
var B = board.create('point', [0,0], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
var C = board.create('point', [1,0], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
var A = board.create('point', [2,1], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
var H = board.create('point', [function(){return B.X()+A.X()-C.X();},function(){return B.Y()+A.Y()-C.Y();}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});

var a1 = board.create('arrow', [B, C]);
a1.setAttribute({strokeColor: '#00FF00'});
var b = board.create('arrow', [C, A]);
b.setAttribute({strokeColor: '#0000FF'});
var c = board.create('arrow', [B, A]);
c.setAttribute({strokeColor: '#00FF00'});

var b2 = board.create('arrow', [B, H]);
b2.setAttribute({strokeColor: '#0000FF'});


var a2 = board.create('arrow', [H, A]);
a2.setAttribute({strokeColor: '#0000FF'});


board.create('text',[function(){return (B.X()+C.X())/2},function(){return (B.Y()+C.Y())/2},"A"]);
board.create('text',[function(){return (C.X()+A.X())/2},function(){return (C.Y()+A.Y())/2},"B"]);
board.create('text',[function(){return (B.X()+A.X())/2},function(){return (B.Y()+A.Y())/2},"C=A+B"]);
board.create('text',[function(){return (B.X()+H.X())/2},function(){return (B.Y()+H.Y())/2},"b"]);

var omega = 2 * Math.PI * 1/10;

function tick(time: number) {
  board.update();
}

function terminate(time: number) {return false;}

function setUp() {}

function tearDown() {popUp.close();}

var runner = eight.animationRunner(tick, terminate, setUp, tearDown, popUp.window);
runner.start();
