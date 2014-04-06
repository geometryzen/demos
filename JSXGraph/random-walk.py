# random-walk.py
from browser import document, window

Math = window.Math

graph = window.JXG.JSXGraph
JXG = window.JXG

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", 
                        {"boundingbox":[-100,100,100,-100],
                         "showCopyright":False,
                         "showNavigation":False})
t = board.create('turtle')
 
def run():
    sumdist=0.0
    stepSize = 5
    board.suspendUpdate()
    nr = 20#document.getElementById('number').value*1
    for i in range(nr):
        t.setPenColor(
                  JXG.hsv2rgb(
                              Math.round(Math.random()*255),
                              Math.random(),
                              Math.random()))
        for j in range(100):
            a = Math.floor(360*Math.random()) 
            t.right(a) 
            t.forward(stepSize)

        dist = t.pos[0]*t.pos[0]+t.pos[1]*t.pos[1]
        sumdist += dist
        t.home()

    print sumdist/nr
    board.unsuspendUpdate()

run()