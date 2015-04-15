graph = JXG.JSXGraph

board = graph.initBoard("box", 
                        "boundingbox":[-100,100,100,-100],
                         "showCopyright":false,
                         "showNavigation":false);
t = board.create('turtle');
 
run = () ->
    sumdist=0.0;
    stepSize = 5;
    board.suspendUpdate();
    walkCount = 20;
    for (i=0; i < walkCount; i++)
        t.setPenColor(
                  JXG.hsv2rgb(
                              Math.round(Math.random()*255),
                              Math.random(),
                              Math.random()));
        for (j=0; j < 100; j++)
            angle = Math.floor(360*Math.random())
            t.right(angle)
            t.forward(stepSize)
        dist = t.pos[0]*t.pos[0]+t.pos[1]*t.pos[1];
        sumdist += dist;
        t.home()

    Sk.output(sumdist/walkCount+"\n");
    board.unsuspendUpdate();

run();
