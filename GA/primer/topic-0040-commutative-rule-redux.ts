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

// Model: Using Euclidean3 right now because __div__ is not there for Euclidean2.
var o = new blade.Euclidean2(0,0,0,0);
var a = new blade.Euclidean2(0,1,0,0);
var b = new blade.Euclidean2(0,1,1,0);

// View
// There will be two free points that act as input controlling the vectors a and b.
var board = graph.initBoard("box", {boundingbox:[-2,2,2,-2], axis:true, grid:true, keepaspectratio: true, showCopyright:false, showNavigation:true, document: popUp.document});

// TODO: These functions could be generalized to visualize multivectors.
function createInputArrow(mv: blade.Euclidean2, color: string) {
  // This construction could be turned into a function...
  var head = board.create('point', [mv.x/2, mv.y/2], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
  var tail = board.create('point', [function(){return -head.X();}, function(){return -head.Y()}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
  tail.hideElement();
  board.create('arrow', [tail, head]).setAttribute({strokeColor: color});
  head.on('drag',function(){mv.x = head.X()*2; mv.y = head.Y()*2});
}

function createOutputArrow(mv: ()=>blade.Euclidean2, color: string) {

    var head = board.create('point', [function(){return mv().x/2;},function(){return mv().y/2;}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
    var tail = board.create('point', [function(){return -head.X();},function(){return -head.Y();}], {withLabel:false, strokeColor:'#CCCCCC', fillOpacity: 0, highlightFillOpacity: 0});
    head.hideElement();
    tail.hideElement();
    board.create('arrow', [tail, head]).setAttribute({strokeColor: color});
}

createInputArrow(a, '#FF0000');
createInputArrow(b, '#00FF00');

createOutputArrow(function(){return a+b;}, '#0000FF');
