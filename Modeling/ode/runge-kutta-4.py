import numpy
from e3ga import *
from time import *
from browser import window

# Set up the standard unit vectors for Cartesian coordinates.
e1 = VectorE3(1, 0, 0)
e2 = VectorE3(0, 1, 0)
e3 = VectorE3(0, 0, 1)

origin = VectorE3(0,0,0)

# Simple Harmonic Motion
def SHO(time, state):
    position = state[0]
    velocity = state[1]
    acceleration = - k/m * position + g - d * velocity
    return numpy.array([velocity, acceleration])

alpha = 0.8

def rungeKutta4(y, x, h, f):
    k1 = h * f(x,y)
    k2 = k1
    # k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
    k3 = k1
    # k3 = h * f(x + 0.5 * h, y + (0.5-(1.0/alpha)) * k1 + (1/alpha) * k2)
    k4 = k1
    # k4 = h * f(x + h, y + (1.0-(alpha/2.0)) * k2 + (alpha/2) * k3)
    return y + (k1 + (4.0-alpha) * k2 + alpha * k3 + k4) / 6.0

N = 1000

# Keep track of displacement and velocity.
y = numpy.zeros((N,2))

# Initial position goes in slot 0. We start at the origin.
y[0,0] = origin
# Initial velocity goes in slot 1. We start from rest.
y[0,1] = VectorE3(0, 0, 0)

tau = 10.0

t = numpy.linspace(0.0, tau, N)

dt = tau / float(N-1)

# Spring constant.
k = 3.5
# Mass of body.
m = 0.2
# Damping
d = 0.0
# Acceleration due to gravity.
g = -9.81 * e3

# Propagate forward in time.
for j in range(N-1):
    y[j+1] = rungeKutta4(y[j], t[j], dt, SHO)

# Extract the data that we need for driving the graph.
dataT = [t[j]   for j in range(N)]    
dataX = [y[j,0].z for j in range(N)]
dataV = [y[j,1].z for j in range(N)]

graph = window.JXG.JSXGraph

window.document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = window.document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

board = graph.initBoard("box", {"boundingbox":[-1.0,5.0,tau,-5],"axis":True,"showCopyright":False})

board.create('curve',[dataT,dataX],{"strokeColor":'blue'})

board.create('curve',[dataT,dataV],{"strokeColor":'green'})
board.create('tapemeasure', [[0,-4], [1,-4]], {"name":'distance'});
print "time now:", time()

print "alpha", alpha
