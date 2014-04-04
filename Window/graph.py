from browser import document
from jxg import JSXGraph

gc = document.getElementById("graph-container")
pc = document.getElementById("printer-container")

div = document.createElement("div")
div.id = "box"
div.style.width = "400px"
div.style.height = "400px"

gc.appendChild(div)

JSXGraph.initBoard("box")
