from browser import window

d3 = window.d3

width = max(960, window.innerWidth)
height = max(500, window.innerHeight)

svg = d3.select("body").append("svg").attr("width", width).attr("height", height)

svg.append("rect")
    .attr("width", width)
    .attr("height", height)
    .on("mousemove", particle)

def particle():
    m = d3.mouse(this);

    svg.insert("circle", "rect")
        .attr("cx", m[0])
        .attr("cy", m[1])
        .attr("r", 1e-6)
        .style("stroke", d3.hsl((i = (i + 1) % 360), 1, .5))
        .style("stroke-opacity", 1)
        .transition()
        .duration(2000)
        .ease(Math.sqrt)
        .attr("r", 100)
        .style("stroke-opacity", 1e-6)
        .remove()

    d3.event.preventDefault()