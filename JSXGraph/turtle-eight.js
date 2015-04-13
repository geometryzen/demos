var JXG = window.JXG;
var graph = JXG.JSXGraph;

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>';
var div = document.getElementById("box");

div.style.width  = "400px";
div.style.height = "400px";

var board = graph.initBoard("box", 
                        {"boundingbox":[-250,250,250,-250],
                         "showCopyright":false,
                         "showNavigation":false});

var t = board.create('turtle',[0, 0], {"strokeOpacity":0.5});

t.setPenSize(3);
t.right(90);
var alpha = 0;
 
function run() {
    t.forward(2);
    if (Math.floor(alpha / 360) % 2 === 0) {
        t.left(1);
    }
    else {
        t.right(1);
    }

    alpha += 1;

    if (alpha < 1440) {
        window.setTimeout(run, 20);
    }
}

run();
