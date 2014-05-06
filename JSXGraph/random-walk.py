from browser import document, window
from random import random

Math = window.Math

graph = window.JXG.JSXGraph
JXG = window.JXG

board = graph.initBoard("box", 
                        {"boundingbox":[-100,100,100,-100],
                         "showCopyright":False,
                         "showNavigation":False})
t = board.create('turtle')
 
def run():
    sumdist=0.0
    stepSize = 5
    board.suspendUpdate()
    walkCount = 20
    for i in range(walkCount):
        t.setPenColor(
                  JXG.hsv2rgb(
                              Math.round(random()*255),
                              random(),
                              random()))
        for j in range(100):
            angle = Math.floor(360*random()) 
            t.right(angle) 
            t.forward(stepSize)

        dist = t.pos[0]*t.pos[0]+t.pos[1]*t.pos[1]
        sumdist += dist
        t.home()

    print sumdist/walkCount
    board.unsuspendUpdate()

run()