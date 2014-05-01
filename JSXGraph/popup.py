from browser import *
from math import *

graph = window.JXG.JSXGraph

win = window.open("","","width=600,height=600")

win.document.body.innerHTML = '<div id="box" class="jxgbox"></div>'

div = win.document.getElementById("box")

print type(win)
print type(win.document)
print type(div)

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", {"document":win.document,"axis":True,"grid":True})

A = board.create('point',[1,1],{"name": 'Alice'})
B = board.create('point',[2,2],{"name":'Bob'})

f = board.create('functiongraph',[lambda x,unused: A.X() * sin(x)])

def tick(time):
    # May be a faster way to make the animation run?
    angle = time*pi*2/10
    A.moveTo([3 * sin(angle),3 * cos(angle)])

def terminate(time):
    return time > 5

def setUp():
    pass

def tearDown():
    win.close()
    print "The window was closed."

WindowAnimationRunner(tick, terminate, setUp, tearDown, win).start()
