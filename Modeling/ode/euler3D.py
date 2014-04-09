# A work in progress.
# Extend the simple euler example by using vectors, show the acceleration, maybe use units, simulation...
import numpy
from e3ga import *
from browser import document, window

# Set up the standard unit vectors for Cartesian coordinates.
e1 = VectorE3(1, 0, 0)
e2 = VectorE3(0, 1, 0)
e3 = VectorE3(0, 0, 1)

#def FreeFall(state,time):
#    g0 = state[1]
#    g1 = -9.8
#    return numpy.array([g0, g1])

# Simple Harmonic Motion
def SHO(state, time):
    g0 = state[1]
    g1 = - k/m * state[0] - gravity
    return numpy.array([g0, g1])

def euler(y, t, dt, derivs):
    d = derivs(y,t)
    dy = d * numpy.array([dt,dt])
    return y + dy

N = 1000

y = numpy.zeros((N,2))

y[0,0] = VectorE3(0,0,0)
y[0,1] = 0.0

tau = 5.0

t = numpy.linspace(0.0, tau, N)

dt = tau / float(N-1)

k = 3.5
m = 0.2
gravity = 9.8

for j in range(N-1):
    y[j+1] = euler(y[j], t[j], dt, SHO)

dataT = [t[j]   for j in range(N)]    
dataX = [y[j,0] for j in range(N)]
dataV = [y[j,1] for j in range(N)]

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = graph.initBoard("box", {"boundingbox":[-1.0,5,5,-5],"axis":True,"showCopyright":False})

b.create('curve',[dataT,dataX],{"strokeColor":'red'})

b.create('curve',[dataT,dataV],{"strokeColor":'blue'})

print "Notice how the energy increases with the Euler solution."
