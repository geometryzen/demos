from browser import document
from jxg import JSXGraph

gc = document.getElementById("graph-container")

div = document.createElement("div")
div.id = "box"

gc.appendChild(div)

print gc
