from browser import document
from jxg import JSXGraph

gc = document.getElementById("graph-container").innerHTML = '<div id="box"></div>'
div = document.getElementById("box")

div.style.width = "400px"
div.style.height = "400px"

JSXGraph.initBoard("box", {"boundingbox":[-2,4,6,-4]})
