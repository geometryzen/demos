from browser import document
from jxg import JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

JSXGraph.initBoard("box", 
                   {"axis":True,
                    "grid":True,
                    "showCopyright":False})
