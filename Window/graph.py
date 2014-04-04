from browser import document
from jxg import JSXGraph

gc = document.getElementById("graph-container")

div = document.createElement("div")
div.id = "box"
div.style.width = "400px"

gc.appendChild(div)

print gc
