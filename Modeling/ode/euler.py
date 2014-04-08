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

y = numpy.zeros([N,2])