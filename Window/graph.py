from browser import document
from jxg import JSXGraph

gc = document.getElementById("graph-container")

div = document.createElement("div")

gc.addChild(div)

print gc
