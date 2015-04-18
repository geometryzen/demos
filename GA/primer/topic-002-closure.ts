var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

var graph = JXG.JSXGraph;

var popUp: Window = open("", "", "width=800, height=600");

var css = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />';
popUp.document.documentElement.innerHTML = css+'<div id="box" class="jxgbox" style="width:800px; height:600px;"></div>'
popUp.document.title = "Vector";
popUp.document.body.style.backgroundColor = "CCCCCC";
popUp.document.body.style.overflow = "hidden";
var div = popUp.document.getElementById("box");

div.style.width  = "760px";
div.style.height = "560px";

var board = graph.initBoard("box", {axis:false, grid:false, keepaspectratio: true, showCopyright:false, showNavigation:false, document: popUp.document});

var pos = new blade.Euclidean2(0,0,0,0);
var vec = new blade.Euclidean2(0,1,0,0);
var tailParents = [function(){return pos.x;}, function(){return pos.y}];
var headParents = [function(){return pos.x+vec.x;}, function(){return pos.y+vec.y}];

// Create an arrow providing two points.
var tail = board.create('point', tailParents, {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0, highlightStrokeColor:'#CCCCCC'});
var head = board.create('point', headParents, {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0, highlightStrokeColor:'#00FF00'});
var arrow = board.create('arrow', [tail, head]);
tail.hideElement();
head.hideElement();
arrow.setAttribute({strokeColor: JXG.hsv2rgb(0,0,0), withLabel:true});
arrow.setLabelText("a");

var omega = 2 * Math.PI * 1/10;

function tick(time: number) {
  vec.x = Math.cos(omega * time);
  vec.y = Math.sin(omega * time);
  board.update();
}

function terminate(time: number) {return false;}

function setUp() {}

function tearDown() {popUp.close();}

var runner = eight.animationRunner(tick, terminate, setUp, tearDown, popUp.window);
runner.start();
