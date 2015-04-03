graph = JXG.JSXGraph;
sin = Math.sin;

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById "box"

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard "box", {"axis":true,"grid":true}

A = board.create 'point',[1,1],{"name": 'Alice'}
B = board.create 'point',[2,2], {"name":'Bob'}

f = board.create 'functiongraph',[(x) -> A.X() * sin(x)]
