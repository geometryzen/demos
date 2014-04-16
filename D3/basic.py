from browser import window

d3 = window.d3

width = max(960, window.innerWidth)
height = max(500, window.innerHeight)

i = 0

svg = d3.select("body").append("svg").attr("width", width).attr("height", height)

def particle():
    m = d3.mouse(this)

    circle = svg.insert("circle", "rect")
    print circle
    circle.attr("cx", m[0])
    circle.attr("cy", m[1])
    circle.attr("r", 1e-6)
#   circle.style("stroke", d3.hsl((i = (i + 1) % 360), 1, .5))
    circle.style("stroke-opacity", 1)
    circle.transition().duration(2000).ease(window.Math.sqrt).attr("r", 100).style("stroke-opacity", 1e-6).remove()

    d3.event.preventDefault()
    
svg.append("rect").attr("width", width).attr("height", height).on("mousemove", particle)
