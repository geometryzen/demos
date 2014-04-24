import numpy
from e3ga import *
from time import *
from units import *
from browser import window

print "time begin:", time()

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
a2 = 4 - alpha
a3 = alpha
b31 = (0.5-(1.0/alpha))
b32 = 1 / alpha
b42 = (1.0-(alpha/2.0))
b43 = alpha / 2

def rungeKutta4(y, x, h, f):
    k1 = h * f(x,y)
    k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
    k3 = h * f(x + 0.5 * h, y + b31 * k1 + b32 * k2)
    k4 = h * f(x + h, y + b42 * k2 + b43 * k3)
    return y + (k1 + a2 * k2 + a3 * k3 + k4) / 6.0

N = 200

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
d = 0.2 * newton / (meter / second)
print "d: %s" % d
# Acceleration due to gravity.
g = -9.81 * e3 * newton / kilogram
print "g: %s" % g

# Propagate forward in time.
for j in range(N-1):
    y[j+1] = rungeKutta4(y[j], t[j], dt, SHO)

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

board.create('curve',[dataT,dataV],{"strokeColor":'red'})
board.create('tapemeasure', [[0,-4], [1,-4]], {"name":'distance'});
print "time end:", time()

print "alpha", alpha
