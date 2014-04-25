from e2ga import *
from units import *
import numpy as np
from browser import window
from math import *

JXG = window.JXG
graph = JXG.JSXGraph

b = graph.initBoard("box", 
                    {"boundingbox": [-10,10,10,-10],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

e1 = VectorE2(1,0)

tail = b.create('point',[0,0], {'name':'A'})
head = b.create('point',[e1.x,e1.y], {'name':'B'})

line = b.create('line',[tail,head], 
 {'straightFirst':False, 'straightLast':False,'lastArrow':True})

txt = b.create('text',[-2,-1, 'Hello World'], {'fontSize':30})
