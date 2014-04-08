def FreeFall(state,time):
    g0 = state[1]
    g1 = -9.8
    return numpy.array([g0, g1])

def euler(y, t, dt, derivs):
    y.next = y + derivs(y,t) * dt
    return y.next