from browser import document
from jxg import JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = JSXGraph.initBoard("box", {"axis":True,"grid":True,"showCopyright":False})

free = board.create('point',[3,4],{"name":'A',"size":3})

def foo():
    return free.X()

bar = lambda: free.X()

dep = board.create('point',[foo,1],{"name":'B',"size":3})

#p.setAttribute({"fixed":True});

print foo()
print free.X()
print free.Y()
