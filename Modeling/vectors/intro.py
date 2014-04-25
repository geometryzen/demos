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

print e1
print e1.x
print e1.y
print repr(e1)
print e1.w
print e1.xy

tail = b.create('point',[-1,1], {'name':'A','size':4})
head = b.create('point',[2,-1], {'name':'B','size':4})
