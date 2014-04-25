from e2ga import *
from units import *
import numpy as np
from browser import *
from math import *
from random import random

JXG = window.JXG
JXG.Options.text.useMathJax = True
graph = JXG.JSXGraph

scale = 100

board = graph.initBoard("box", 
                    {"boundingbox": [-scale,scale,scale,-scale],
                     "axis":False,
                     "showCopyright":False,
                     "showNavigation":False
                     })

a = VectorE2(scale/2,0)
b = VectorE2(0,scale/2)
c = a + b
A = None
B = None
C = None

def toString(name, mv):
    return "\\[\\vec{%s}=%s\\]" % (name, str(mv / scale))
    return "\\[ %s_x=%0.3f, %s_y=%0.3f \\]" % (name, mv.x, name, mv.y)

def Arrow(name, vector, x, y, color):
    pointDef = {'name':'',
                'size':5,
                'fillOpacity':0.3,
                'strokeOpacity':0.3,
                'strokeColor':'gray',
                'fillColor':'gray',
                'snapToGrid':True}
    tail = board.create('point',[random()*scale/2, random()*scale/2], pointDef)
    head = board.create('point',[tail.X() + vector.x, tail.Y() + vector.y], pointDef)
    txt = board.create('text',[x, y, lambda: toString(name, vector)], {'fontSize':20, 'strokeColor':color,'fixed':True})
    return board.create('arrow',[tail,head],{'strokeWidth':5, 'strokeOpacity':0.7, 'strokeColor':color,'snapToGrid':True});

def updateVector(vector, arrow):
    vector.x = arrow.point1.X() - arrow.point2.X()
    vector.y = arrow.point1.Y() - arrow.point2.Y()

def tick():
    updateVector(a, A)
    updateVector(b, B)
    updateVector(c, C)

def terminate():
    pass

def setUp():
    print "Press Esc to terminate."
    global A, B, C
    A = Arrow('a', a, -scale, -0.5 * scale, 'red')
    B = Arrow('b', b, -scale, -0.6 * scale, 'green')
    C = Arrow('c', c, -scale, -0.7 * scale, 'blue')

def tearDown():
    print "Goodbye!"
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
