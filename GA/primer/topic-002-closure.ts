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

// Create an arrow providing two points.
var B = board.create('point', [0,0], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
var C = board.create('point', [1,0], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
var A = board.create('point', [2,1], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});

var a = board.create('arrow', [B, C]);
a.setAttribute({strokeColor: '#FF0000', withLabel:true});
a.setLabelText("A");
var b = board.create('arrow', [C, A]);
b.setAttribute({strokeColor: '#0000FF', withLabel:true});
b.setLabelText("B");

var omega = 2 * Math.PI * 1/10;

function tick(time: number) {
  board.update();
}

function terminate(time: number) {return false;}

function setUp() {}

function tearDown() {popUp.close();}

var runner = eight.animationRunner(tick, terminate, setUp, tearDown, popUp.window);
runner.start();
