class Gravity:
"""Gravity force between two physical objects."""

def __init__(self, m, M):
    self.m = m # mass of object 1
    self.M = M # mass of object 2
    self.G = 6.67428E-11 # gravity constant, m**3/kg/s**2

def force(self, r):
    G, m, M = self.G, self.m, self.M
    return G*m*M/r**2

def visualize(self, r_start, r_stop, n=100):
    #from numpy import linspace
    #r = linspace(r_start, r_stop, n)
    r = [1,2,3,4,5,6,7]
    g = self.force(r)
    title='Gravity force: m=%g, M=%g' % (self.m, self.M)
    #plot(r, g, title=title)
class CoulumbsLaw(Gravity):
def init(self, q1, q2):
Gravity.init(self, q1, q2)
self.G = 8.99E9

c = CoulumbsLaw(1E-6, -2E-6)
print 'Electric force:', c.force(0.1)
c.visualize(0.01, 0.2)