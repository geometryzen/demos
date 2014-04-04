from browser import document, window
from jxg import require

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = JSXGraph.initBoard("box", {"boundingbox":[-5,5,5,-5]})

p1 = b.create('point',[0,0],{"name":'A',"size":4})
p2 = b.create('point',[ 2,-1],{"name":'B',"size":4})

ci = b.create(
    'circle',
    [p1,p2],
    {
        "fillColor":"#555500",
        "dash":2,
        "fillOpacity": lambda: p2.X() * 0.25
    }
)

print window.JXG
