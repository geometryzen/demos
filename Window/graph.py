from browser import document
from jxg import JSXGraph

gc = document.getElementById("graph-container").innerHtml = ""
pc = document.getElementById("printer-container")

div = document.createElement("div")
div.id = "box"
div.style.width = "400px"
div.style.height = "400px"

gc.appendChild(div)

JSXGraph.initBoard("box", {"boundingbox":[-2,4,6,-4]})
