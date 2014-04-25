from e2ga import *
from units import *
import numpy as np
from browser import *
from math import *

JXG = window.JXG
JXG.Options.text.useMathJax = True
graph = JXG.JSXGraph

board = graph.initBoard("box", 
                    {"boundingbox": [-2,2,2,-2],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

a = VectorE2(1,0)
b = VectorE2(0,1)
c = a + b
A = None
B = None
C = None

def toString(mv):
    return "\\[ a_x=%0.3f, a_y=%0.3f \\]" % (mv.x, mv.y)

def Arrow(x, color):
    pointDef = {'name':'','size':5,'fillOpacity':0.3,'strokeOpacity':0.3,'strokeColor':'gray','fillColor':'gray'}
    tail = board.create('point',[0,0], pointDef)
    head = board.create('point',[a.x,a.y], pointDef)
    txt = board.create('text',[-1.5,+1.5, lambda: toString(a)], {'fontSize':20, 'strokeColor':color})
    return board.create('arrow',[tail,head],{'strokeWidth':5, 'strokeOpacity':0.7, 'strokeColor':color});


def tick():
    # Modify the vector to track the User Interface.
    a.x = A.point1.X() - A.point2.X()
    a.y = A.point1.Y() - A.point2.Y()

def terminate():
    pass

def setUp():
    global A
    A = Arrow(-1.5, 'red')
    B = Arrow(-1.5, 'blue')
    C = Arrow(-1.5, 'green')
    print "Press Esc to terminate."

def tearDown():
    print "Goodbye!"
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
