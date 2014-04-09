import numpy
from browser import document, window
from math import *

def FreeFall(state,time):
    g0 = state[1]
    g1 = -9.8
    return numpy.array([g0, g1])

def SHO(state, time):
    g0 = state[1]
    g1 = - k/m * state[0] - gravity
    return numpy.array([g0, g1])

def euler(y, t, dt, derivs):
    d = derivs(y,t)
    dy = d * numpy.array([dt,dt])
    return y + dy

N = 1000
x0 = 0.0
v0 = 0.0

tau = 3.0

dt = tau / float(N-1)

k = 3.5
m = 0.2
gravity = 9.8

time = numpy.linspace(0.0, tau, N)

y = numpy.zeros((N,2))

y[0,0] = x0
y[0,1] = v0

for j in range(N-1):
    y[j+1] = euler(y[j], time[j], dt, SHO)
    
xdata = [y[j,0] for j in range(N)]
vdata = [y[j,1] for j in range(N)]

print "Done!"

graph = window.JXG.JSXGraph

document.getElementById("graph-container").innerHTML = '<div id="box" class="jxgbox"></div>'
div = document.getElementById("box")

div.style.width  = "400px"
div.style.height = "400px"

b = graph.initBoard("box", {"boundingbox":[-10,10,20,-10],"axis":True})

p = b.create('point',[1,4])
dataX = [1,2,3,4,5,6,7,8]
dataY = [0.3,4.0,-1,2.3,7,9,8,9]

b.create('curve',[dataX,dataY],{"strokeColor":'red'})
b.create('curve',[dataX,lambda x: p.X()*sin(x)*x],{"strokeColor":'blue',"dash":1})
