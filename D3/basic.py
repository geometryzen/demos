from browser import *
from workbench import *
import math

d3 = window.d3

d3.select("body").style("background-color", "#222")

width = max(960, window.innerWidth)
height = max(500, window.innerHeight)
x1 = width / 2
y1 = height / 2
x0 = x1
y0 = y1
x = x0
y = y0
i = 0
r = 200
c = ""
tau = math.pi * 2

canvas = d3.select("body").append("canvas")
canvas.attr("width", width).attr("height", height)

workbench = Workbench2D(canvas.node())

context = canvas.node().getContext("2d")
context.globalCompositionOperation = "lighter"
context.lineWidth = 6
print context.lineWidth
print context.globalCompositionOperation

def circle(t):
    s = c + str(1-t) + ")"
    context.strokeStyle = "rgba(255.0,100.0,255.0,"+str(1-t)+")"
    context.beginPath()
    context.arc(x, y, r * t, 0, tau)
    context.stroke()
    pass

def tweeny():
    return circle

def setUp():
    workbench.setUp()

def tick(t):
    global i, x0, y0, c,x,y
    i += 1
    context.clearRect(0,0,width,height)
    z = d3.hsl(i % 360, 1, 0.5).rgb()
    c = "rgba(" + str(z.r) + "," + str(z.g) + "," + str(z.b) + ","
    x0 += (x1 - x0) * .1
    y0 += (y1 - y0) * .1
    x = x0
    y = y0
    d3.select({}).transition().duration(2000).ease(math.sqrt).tween("circle", tweeny)
    pass

def terminate(t):
    return t > 10
    
def tearDown():
    workbench.tearDown()

war = WindowAnimationRunner(tick, terminate, setUp, tearDown)
war.start()

