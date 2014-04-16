from browser import *
from workbench import *
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

canvas = document.createElement("canvas")

workbench = Workbench2D(canvas)

context = canvas.getContext("2d")

progressEnd = 3
        
step = 0
steps = 50
addAngle = 2 * pi / steps
addScale = 1.0 / steps

def setUp():
    workbench.setUp()

def tick(t):
    global step
    if step < steps:
        step += 1
    # Changing the canvas width or height resets the canvas.
    context.fillStyle = "blue"
    context.font = "24pt Helvetica"
    context.textAlign = "center"
    context.textBaseline = "middle"
    context.clearRect(0, 0, canvas.width, canvas.height)
    context.save()
    context.translate(canvas.width / 2, canvas.height / 2)
    context.scale(addScale * step, addScale * step)
    context.rotate(addAngle * step)
    context.fillText("Geometry Zen", 0, 0)
    context.restore()

def terminate(t):
    return t > progressEnd
    
def tearDown():
    workbench.tearDown()

war = WindowAnimationRunner(tick, terminate, setUp, tearDown)
war.start()

