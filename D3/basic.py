from browser import window

d3 = window.d3

width = max(960, window.innerWidth)
height = max(500, window.innerHeight)

svg = d3.select("body").append("svg").attr("width", width).attr("height",height)