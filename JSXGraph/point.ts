var graph = JXG.JSXGraph;

function out(x: string) {
  var w: any = window;
  w.Sk.output(x + "\n");
}
var popUp: Window = open("", "", "width=800, height=600");

var css = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />';
popUp.document.documentElement.innerHTML = css+'<div id="box" class="jxgbox" style="width:800px; height:600px;"></div>'
popUp.document.title = "JXG.Ellipse";
popUp.document.body.style.backgroundColor = "CCCCCC";
popUp.document.body.style.overflow = "hidden";
var div = popUp.document.getElementById("box");

div.style.width  = "760px";
div.style.height = "560px";

var board = graph.initBoard("box", {axis:true, grid:true, keepaspectratio: true, showCopyright:false, document: popUp.document});

var point: JXG.Point = board.create('point', [0,0]);

point.setName("E");

out(point.getName()+"\n");

function tick(time: number) {
  point.moveTo([1,2])
    // We can use the variables to drive other windows!
    var x: number = point.X();
    var y: number = point.Y();
}

function terminate(time: number) {
  return false;
}

function setUp() {
  
}

function tearDown(e: Error) {
  popUp.close();
}

// May need to make sure that JSXGraph and animationRunner play well together?
var war = eight.animationRunner(tick, terminate, setUp, tearDown, popUp.window);
war.start();
