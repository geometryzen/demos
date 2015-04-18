var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

log(JXG.hsv2rgb(0,1,1));

var graph = JXG.JSXGraph;

var popUp: Window = open("", "", "width=800, height=600");

var css = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />';
popUp.document.documentElement.innerHTML = css+'<div id="box" class="jxgbox" style="width:800px; height:600px;"></div>'
popUp.document.title = "JXG.Arrow";
popUp.document.body.style.backgroundColor = "CCCCCC";
popUp.document.body.style.overflow = "hidden";
var div = popUp.document.getElementById("box");

div.style.width  = "760px";
div.style.height = "560px";

var board = graph.initBoard("box", {axis:false, grid:false, keepaspectratio: true, showCopyright:false, showNavigation:false, document: popUp.document});

// Create an arrow providing two points.
var tail = board.create('point', [0.0, 0.0], {withLabel:false, strokeColor:'#00AA00',fillColor:'#00FF00',fillOpacity:0});
var head = board.create('point', [1.0, 0.0], {withLabel:false});
var arrow = board.create('arrow', [tail, head]);
//tail.hideElement();
//head.hideElement();
arrow.setAttribute({strokeColor: JXG.hsv2rgb(0,0,0), withLabel:true});
arrow.setLabelText("a");

function tick(time: number) {
    // We can use the variables to drive other windows!
}

function terminate(time: number) {
  return false;
}

function setUp() {
  
}

function tearDown() {
  popUp.close();
}

// May need to make sure that JSXGraph and animationRunner play well together?
var war = eight.animationRunner(tick, terminate, setUp, tearDown, popUp.window);
war.start();