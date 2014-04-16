from browser import *
from workbench import *
import math

d3 = window.d3

width = max(960, window.innerWidth)
height = max(500, window.innerHeight)

canvas = d3.select("body").append("canvas")
canvas.attr("width", width).attr("height", height)

workbench = Workbench2D(canvas.node())

context = canvas.node().getContext("2d")

def setUp():
    workbench.setUp()

def tick(t):
    context.clearRect(0,0,width,height)
    pass

def terminate(t):
    return t > 10
    
def tearDown():
    workbench.tearDown()

war = WindowAnimationRunner(tick, terminate, setUp, tearDown)
war.start()

