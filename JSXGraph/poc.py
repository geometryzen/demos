from browser import document
from jxg import JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = JSXGraph.initBoard("box", {"axis":True,"grid":True,"showCopyright":False})

free = board.create('point',[0,0],{"name":'A',"size":3})
dep = board.create('point',["X(A)",1],{"name":'B',"size":3})

#p.setAttribute({"fixed":True});

print free.X()
