var graph = JXG.JSXGraph;
var sin = Math.sin;

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
var div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

var board = graph.initBoard("box", {axis:true,grid:true, showCopyright:false})

// Parametric curve
// Create a curve of the form (t-sin(t), 1-cos(t), i.e.
// the cycloid curve.
  var curve = board.create('curve',
                       [function(t){ return t-Math.sin(t);},
                        function(t){ return 1-Math.cos(t);},
                        0, 2*Math.PI]
                    );