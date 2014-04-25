from e2ga import *
from units import *
import numpy as np
from browser import *
from math import *

JXG = window.JXG
graph = JXG.JSXGraph

board = graph.initBoard("box", 
                    {"boundingbox": [-2,2,2,-2],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

a = VectorE2(1,1)

tail = board.create('point',[0,0], {'size':5,'fillOpacity':0.3,'strokeOpacity':0.3})
head = board.create('point',[a.x,a.y], {'size':5,'fillOpacity':0.3,'strokeOpacity':0.3})

line = board.create('arrow',[tail,head],{'strokeWidth':5, 'strokeOpacity':0.7, 'strokeColor':'blue'});

def toString(geo):
    return repr(geo)

txt = board.create('text',[-1.5,+1.5, toString(a)], {'fontSize':30})

def tick():
    a.x = head.X() - tail.X()
    a.y = head.Y() - tail.Y()

def terminate():
    pass

def setUp():
    print "Press Esc to terminate."

def tearDown():
    print "Goodbye!"
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
