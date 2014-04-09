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
def SHO(state, time):
    position = state[0]
    velocity = state[1]
    acceleration = - k/m * position + g - b * velocity
    return numpy.array([velocity, acceleration])

# TODO: Let's record the acceleration.
def euler(y, t, dt, derivs):
    d = derivs(y,t)
    # TODO: Would be nice to be able to do scalar multiplication here.
    dy = d * numpy.array([dt,dt])
    return y + dy

N = 1000

# Keep track of displacement and velocity.
y = numpy.zeros((N,2))

# Initial position goes in slot 0. We start at the origin.
y[0,0] = origin
# Initial velocity goes in slot 1. We start from rest.
y[0,1] = VectorE3(0, 0, 0)

tau = 5.0

t = numpy.linspace(0.0, tau, N)

dt = tau / float(N-1)

# Spring constant.
k = 3.5
# Mass of body.
m = 0.2
# Drag
b = 1.0
# Acceleration due to gravity.
g = -9.81 * e3

# Propagate forward in time.
for j in range(N-1):
    y[j+1] = euler(y[j], t[j], dt, SHO)

# Extract the data that we need for driving the graph.
dataT = [t[j]   for j in range(N)]    
dataX = [y[j,0].z for j in range(N)]
dataV = [y[j,1].z for j in range(N)]

graph = window.JXG.JSXGraph

window.document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = window.document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = graph.initBoard("box", {"boundingbox":[-1.0,5,6,-5],"axis":True,"showCopyright":False})

b.create('curve',[dataT,dataX],{"strokeColor":'blue'})

b.create('curve',[dataT,dataV],{"strokeColor":'green'})

print "time now:", time()
print "Notice how the energy increases with the Euler solution."
