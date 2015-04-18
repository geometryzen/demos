// In the previous commutative rule demonstration, we did not really show that a+b=c+a.
// We now use the JXG visual elements to update a model (the underlying mathematical structures)
// which is then used to update the view.
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

// Model
var o = new blade.Euclidean2(0,0,0,0);
var a = new blade.Euclidean2(0,1,0,0);
var b = new blade.Euclidean2(0,1,1,0);

// View
// There will be two free points that act as input controlling the vectors a and b.
var board = graph.initBoard("box", {boundingbox:[-1,2,3,-1], axis:true, grid:true, keepaspectratio: true, showCopyright:false, showNavigation:true, document: popUp.document});

function createArrow(initial: blade.Euclidean2): JXG.Point {
  // This construction could be turned into a function...
  var head = board.create('point', [initial.x/2, initial.y/2], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
  var tail = board.create('point', [function(){return -head.X();}, function(){return -head.Y()}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
  tail.hideElement();
  board.create('arrow', [tail, head]).setAttribute({strokeColor: '#FF0000'});
  return head;
}

var AHead = createArrow(a);


/*
var C = board.create('point', [1,0], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
var A = board.create('point', [2,1], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});

var H = board.create('point', [function(){return b.x;},function(){return b.y;}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
H.hideElement();
var F = board.create('point', [function(){return (b+a).x;},function(){return (b+a).y;}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});

var a1 = board.create('arrow', [B, C]);
a1.setAttribute({strokeColor: '#00FF00'});
var b1 = board.create('arrow', [C, A]);
b1.setAttribute({strokeColor: '#00FF00'});

var c = board.create('arrow', [B, A]);
c.setAttribute({strokeColor: '#FF0000'});

var b2 = board.create('arrow', [B, H]);
b2.setAttribute({strokeColor: '#0000FF'});


var a2 = board.create('arrow', [H, A]);
a2.setAttribute({strokeColor: '#0000FF'});


board.create('text',[function(){return (B.X()+C.X())/2},function(){return (B.Y()+C.Y())/2},"a"]);
board.create('text',[function(){return (C.X()+A.X())/2},function(){return (C.Y()+A.Y())/2},"b"]);
board.create('text',[function(){return (B.X()+A.X())/2},function(){return (B.Y()+A.Y())/2},"c"]);
board.create('text',[function(){return (A.X()+H.X())/2},function(){return (A.Y()+H.Y())/2},"a"]);
board.create('text',[function(){return (B.X()+H.X())/2},function(){return (B.Y()+H.Y())/2},"b"]);
*/
var omega = 2 * Math.PI * 1/10;

function tick(time: number) {
  // Update the model from the view.
  a.x = AHead.X() * 2;
  a.y = AHead.Y() * 2;
  board.update();
}

function terminate(time: number) {return false;}

function setUp() {}

function tearDown() {popUp.close();}

var runner = eight.animationRunner(tick, terminate, setUp, tearDown, popUp.window);
runner.start();
