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
r = 200
tau = math.pi * 2

canvas = d3.select("body").append("canvas")

canvas.attr("width", width).attr("height", height)

d3.select("canvas").style("background-color", "#222")

def move(unused1, unused2, unused3):
    global x1, y1
    mouse = d3.mouse(canvas.node())
    x1 = mouse[0]
    y1 = mouse[1]
    d3.event.preventDefault()

canvas.on("mousemove", move)

workbench = Workbench2D(canvas.node())

context = canvas.node().getContext("2d")
context.globalCompositeOperation = "lighter"
context.lineWidth = 2

def setUp():
    workbench.setUp()

def tick(t):
    global i, x0, y0
    i += 1
    context.clearRect(0,0,width,height)
    z = d3.hsl(i % 360, 1, 0.5).rgb()
    c = "rgba(" + str(int(z.r)) + "," + str(int(z.g)) + "," + str(int(z.b)) + ","
    x0 += (x1 - x0) * .1
    y0 += (y1 - y0) * .1
    x = x0
    y = y0
    def tweeny(unused1, unused2):
        # This side effect is necessary to make things work!
        a = x
        def circle(t):
            s = c + str(1-t) + ")"
            context.strokeStyle = s
            context.beginPath()
            context.arc(x, y, r * t, 0, tau)
            context.stroke()
        return circle
    d3.select({}).transition().duration(2000).ease(math.sqrt).tween("circle", tweeny)

def terminate(t):
    return t > 60
    
def tearDown(e):
    workbench.tearDown()
    if e:
        print "Ending with exception: " + str(e)

war = WindowAnimationRunner(tick, terminate, setUp, tearDown, window)
war.start()
