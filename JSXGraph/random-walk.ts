var graph = JXG.JSXGraph

var board = graph.initBoard("box", 
                        {"boundingbox":[-100,100,100,-100],
                         "showCopyright":false,
                         "showNavigation":false})
var t = board.create('turtle')
 
function run() {
    var sumdist=0.0;
    var stepSize = 5;
    board.suspendUpdate()
    var walkCount = 20
    for (var i=0; i < walkCount; i++) {
        t.setPenColor(
                  JXG.hsv2rgb(
                              Math.round(Math.random()*255),
                              Math.random(),
                              Math.random()))
        for (var j=0; j < 100; j++) {
            var angle = Math.floor(360*Math.random()) 
            t.right(angle) 
            t.forward(stepSize)
        }
        var dist = t.pos[0]*t.pos[0]+t.pos[1]*t.pos[1]
        sumdist += dist
        t.home()
    }
    w.Sk.output(sumdist/walkCount+"\n");
    board.unsuspendUpdate()
}
run()