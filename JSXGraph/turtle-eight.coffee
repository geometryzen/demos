JXG = window.JXG;
graph = JXG.JSXGraph;

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>';
div = document.getElementById("box");

div.style.width  = "400px";
div.style.height = "400px";

board = graph.initBoard("box", 
                        {"boundingbox":[-250,250,250,-250], "showCopyright": false, "showNavigation":false});

t = board.create('turtle',[0, 0], {"strokeOpacity":0.5});

t.setPenSize(3);
t.right(90);
alpha = 0;
 
run() => 
    t.forward(2);
    if (Math.floor(alpha / 360) % 2 == 0)
        t.left(1);
    else
        t.right(1)

    alpha += 1;

    if (alpha < 1440)
        window.setTimeout(run, 20);

run();
