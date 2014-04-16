from browser import window

d3 = window.d3

width = max(960, window.innerWidth)
height = max(500, window.innerHeight)

i = 0
rect = None

svg = d3.select("body").append("svg")
svg.attr("width", width).attr("height", height)

def particle():

    global i
    i = (i + 1) % 360
    
    m = d3.mouse(svg)
    print m[0],m[1]
'''

    circle = svg.insert("circle", "rect")
    print circle
    circle.attr("cx", m[0])
    circle.attr("cy", m[1])
    circle.attr("r", 1e-6)
    circle.style("stroke", d3.hsl(i, 1, .5))
    circle.style("stroke-opacity", 1)
    circle.transition().duration(2000).ease(window.Math.sqrt).attr("r", 100).style("stroke-opacity", 1e-6).remove()

    d3.event.preventDefault()
'''
    
rect = svg.append("rect")
rect.attr("width", width).attr("height", height).on("mousemove", particle)
