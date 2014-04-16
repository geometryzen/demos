from browser import *
from workbench import *
import math

d3 = window.d3

width = max(960, window.innerWidth)
height = max(500, window.innerHeight)
x1 = width / 2
y1 = height / 2
x0 = x1
y0 = y1
i = 0

canvas = d3.select("body").append("canvas")
canvas.attr("width", width).attr("height", height)

workbench = Workbench2D(canvas.node())

context = canvas.node().getContext("2d")
context.globalCompositionOperation = "lighter"
context.lineWidth = 2

def circle(t):
    
    pass

def setUp():
    workbench.setUp()

def tick(t):
    global i, x0, y0
    i += 1
    context.clearRect(0,0,width,height)
    z = d3.hsl(i % 360, 1, 0.5).rgb()
    c = "rgba(" + str(z.r) + "," + str(z.g) + "," + str(z.b) + ","
    x0 += (x1 - x0) * .1
    y0 += (y1 - y0) * .1
    x = x0
    y = y0
    d3.select({}).transition().duration(2000).tween("circle")
    print "Excellent"
    pass

def terminate(t):
    return t > 4
    
def tearDown():
    workbench.tearDown()

war = WindowAnimationRunner(tick, terminate, setUp, tearDown)
war.start()

