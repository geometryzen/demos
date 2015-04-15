var graph = JXG.JSXGraph;

// Experiment with an alternative 'type-safe' API.
class Board {
    constructor(public board: JXG.Board) {
      
    }
    point(x: number, y: number): JXG.Point {
        return this.board.create("point", [x, y]);
    }
    arrow(p1: JXG.Point, p2: JXG.Point): JXG.Arrow {
        return this.board.create("arrow",[p1,p2]);
    }
}

var popUp: Window = open("", "", "width=800, height=600");

var css = '<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />';
popUp.document.documentElement.innerHTML = css+'<div id="box" class="jxgbox" style="width:800px; height:600px;"></div>'
popUp.document.title = "JXG.Arrow";
popUp.document.body.style.backgroundColor = "CCCCCC";
popUp.document.body.style.overflow = "hidden";
var div = popUp.document.getElementById("box");

div.style.width  = "760px";
div.style.height = "560px";

var b = graph.initBoard("box", {axis:true, grid:true, keepaspectratio: true, showCopyright:false, document: popUp.document});
var board = new Board(b);

// Create an arrow providing two points.
var p1 = board.point(4.5, 2.0);
var p2 = board.point(1.0, 1.0);
var arrow = board.arrow(p1, p2);

arrow.snapToGrid = true;

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