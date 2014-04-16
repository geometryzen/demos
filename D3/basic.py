from browser import *
from workbench import *
import math

d3 = window.d3

width = max(960, window.innerWidth)
height = max(500, window.innerHeight)

i = 0

canvas = d3.select("body").append("canvas")
canvas.attr("width", width).attr("height", height)

workbench = Workbench2D(canvas.node())

context = canvas.node().getContext("2d")
context.globalCompositionOperation = "lighter"
context.lineWidth = 2

def setUp():
    workbench.setUp()

def tick(t):
    global i
    ++i
    context.clearRect(0,0,width,height)
    z = d3.hsl(i % 360, 1, 0.5).rgb()
    print z
    pass

def terminate(t):
    return t > 4
    
def tearDown():
    workbench.tearDown()

war = WindowAnimationRunner(tick, terminate, setUp, tearDown)
war.start()

