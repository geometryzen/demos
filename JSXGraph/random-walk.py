# random-walk.py
from browser import document, window

Math = window.Math

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", 
                        {"boundingbox":[-100,100,100,-100],
                         "showCopyright":False,
                         "showNavigation":False})
t = board.create('turtle')

t.setPenSize(3)
t.right(90)
alpha = 0
 
def run():
    global alpha
    t.forward(2)
    if (Math.floor(alpha / 360) % 2 == 0):
        t.left(1)
    else:
        t.right(1)

    alpha += 1

    if (alpha < 1440):
        window.setTimeout(run, 20)

run()