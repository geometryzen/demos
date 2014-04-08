import numpy

def FreeFall(state,time):
    g0 = state[1]
    g1 = -9.8
    return numpy.array([g0, g1])

def euler(y, t, dt, derivs):
    y.next = y + derivs(y,t) * dt
    return y.next

N = 1000
x0 = 0.0
v0 = 0.0

tau = 3.0

dt = tau / float(N-1)

k = 3.5
m = 0.2
gravity = 9.8

#time = linspace(0, tau, N)

# Check this...
y = numpy.zeros((N,2))

y[0,0] = x0
y[0,1] = v0

def SHO(state, time):
    g0 = state[1]
    g1 = - k/m * state[0] - gravity
    return numpy.array([g0, g1])

for j in range(N-1):
    y[j+1] = euler(y[j], time[j], dt, SHO)
    
xdata = [y[j,0] for j in range(N)]
vdata = [y[j,1] for j in range(N)]

print vdata