import numpy
from e3ga import *
from time import *
from units import *
from browser import window

# Set up the standard unit vectors for Cartesian coordinates.
e1 = VectorE3(1, 0, 0)
e2 = VectorE3(0, 1, 0)
e3 = VectorE3(0, 0, 1)

origin = VectorE3(0,0,0) * meter
print "origin: %s" % origin

# Simple Harmonic Motion
def SHO(time, state):
    position = state[0]
    velocity = state[1]
    acceleration = - k/m * position + g - (d * velocity)/m
    return numpy.array([velocity, acceleration])

alpha = 0.8
b = 1.0 / (2.0 * alpha)
a = 1.0 - b

def rungeKutta2(y, x, h, f):
    print type(y[0])
    print type(x)
    print type(h)
    print type(f(x,y)[0])
    k1 = h * f(x,y)
    xArg = x + alpha * h
    k2 = h * f(x + alpha * h, y + alpha * k1)
    return y + a * k1 + b * k2

N = 1000

# Keep track of displacement and velocity.
y = numpy.zeros((N,2))

# Initial position goes in slot 0. We start at the origin.
y[0,0] = origin
# Initial velocity goes in slot 1. We start from rest.
y[0,1] = VectorE3(0, 0, 0) * meter / second
print "y[0]: %s" % y[0]

tau = 10.0 * second

t = numpy.linspace(0.0 * second, tau, N)

dt = tau / float(N-1)

print "dt: %s" % dt

# Spring constant.
k = 3.5 * newton / meter
print "k: %s" % k
# Mass of body.
m = 0.2 * kilogram
print "m: %s" % m
# Damping
d = 0.0 * newton / (meter / second)
print "d: %s" % d
# Acceleration due to gravity.
g = -9.81 * e3 * newton / kilogram
print "g: %s" % g

# Propagate forward in time.
for j in range(N-1):
    y[j+1] = rungeKutta2(y[j], t[j], dt, SHO)

# Extract the data that we need for driving the graph.
dataT = [t[j].quantity   for j in range(N)]    
dataX = [y[j,0].quantity.z for j in range(N)]
dataV = [y[j,1].quantity.z for j in range(N)]

graph = window.JXG.JSXGraph

window.document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = window.document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", {"boundingbox":[-1.0,5.0,tau.quantity,-5],"axis":True,"showCopyright":False})

board.create('curve',[dataT,dataX],{"strokeColor":'blue'})

board.create('curve',[dataT,dataV],{"strokeColor":'green'})
board.create('tapemeasure', [[0,-4], [1,-4]], {"name":'distance'});
print "time now:", time()

print "alpha", alpha
print "a", a
print "b", b
