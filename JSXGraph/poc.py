from browser import document
from jxg import JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = JSXGraph.initBoard("box", {"axis":True,"grid":True,"showCopyright":False})

p = board.create('point',[1,2],{name:'X',size:3})
