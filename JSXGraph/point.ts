var graph = JXG.JSXGraph;

function out(x: string) {
  var w: any = window;
  w.Sk.output(x + "\n");
}
var popUp: Window = open("", "", "width=800, height=600");

var css = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />';
popUp.document.documentElement.innerHTML = css+'<div id="box" class="jxgbox" style="width:800px; height:600px;"></div>'
popUp.document.title = "JXG.Point";
popUp.document.body.style.backgroundColor = "FFFFFF";
popUp.document.body.style.overflow = "hidden";
var div = popUp.document.getElementById("box");

div.style.width  = "760px";
div.style.height = "560px";

var board = graph.initBoard("box", {axis:true,
                                    grid:true,
                                    keepaspectratio: true,
                                    showCopyright:false,
                                    showNavigation: false,
                                    document: popUp.document});

var E: JXG.Point = board.create('point',[0,0]);

E.setName("E");

var omega = 2 * Math.PI * (1/10);
var R = 4;

function tick(time: number) {
    var theta = omega * time;
    var x = R * Math.cos(theta);
    var y = R * Math.sin(theta);
    E.moveTo([0, y]);
}

function terminate(time: number) {
  return false;
}

function setUp() {
}

function tearDown(e: Error) {
    popUp.close();
}

var runner = eight.animationRunner(tick, terminate, setUp, tearDown, popUp.window);
runner.start();
