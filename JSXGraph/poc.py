from browser import document
from jxg import JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = JSXGraph.initBoard("box", {"axis":True,"grid":True,"boundingbox":[-5,2,5,-2]})

p1 = b.create('point',[-1,1],{"name":'A',"size":4})
p2 = b.create('point',[ 2,-1],{"name":'B',"size":4})

li = b.create('line',[p1,p2],{"strokecolor":"#00ff00", "dash":2})
