from units import *
import numpy as np
from browser import window
from math import *

JXG = window.JXG
graph = JXG.JSXGraph

b = graph.initBoard("box", 
                    {"boundingbox": [-1,1,1,-1],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })
