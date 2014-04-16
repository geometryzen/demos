from browser import window
import math

d3 = window.d3

width = max(960, window.innerWidth)
height = max(500, window.innerHeight)

i = 250
rect = None

print d3.hsl(i,1,.5)

svg = d3.select("body").append("svg")
svg.attr("width", width).attr("height", height)

def sqrt(x):
    return math.sqrt(x)    

def particle():

    global i
    i = (i + 1) % 360
    
    x = 0#d3.event.pageX
    y = 0#d3.event.pageY

#    m = d3.mouse(svg)
#    print m[0],m[1]

    circle = svg.insert("circle", "rect")

    circle.attr("cx", x)
    circle.attr("cy", y)
    circle.attr("r", 1e-6)
    circle.style("stroke", d3.hsl(i, 1, .5))
    circle.style("stroke-opacity", 1)
    circle.transition().duration(2000).ease(sqrt).attr("r", 100).style("stroke-opacity", 1e-6).remove()

    #d3.event.preventDefault()

    

#rect = svg.append("rect")
#rect.attr("width", width).attr("height", height)#.on("mousemove", particle)

particle()
