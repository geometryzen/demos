from browser import document, window
import jxg
from math import *

JSXGraph = jxg.require('JXG').JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = JSXGraph.initBoard("box", {"boundingbox":[-10,10,20,-10],"axis":True})

p = b.create('point',[1,4])
dataX = [1,2,3,4,5,6,7,8]
dataY = [0.3,4.0,-1,2.3,7,9,8,9]

# It does seem that JXG calls with a second Boolean argument.
def foo(x, unused):
    print x, unused
    return p.X() * sin(x) * x

b.create('curve',[dataX,dataY],{"strokeColor":'red'})

# FIXME: Some bug prevents us from doing this.
b.create('curve',[dataX,foo],{"strokeColor":'blue',"dash":1})
