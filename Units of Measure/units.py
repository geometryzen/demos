from math import *
from units import *

omega = 2 * pi / (10 * second)

print repr(omega)
print omega

elapsed = 5000 # % milliseconds

t = elapsed * second / 1000

print repr(t)
print t

angle = omega * t

print repr(angle)
print angle

c = angle.cos()
#c = cos(angle)

