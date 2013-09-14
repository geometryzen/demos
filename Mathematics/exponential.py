from e3ga import *
from math import exp, pi
from units import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
theta = pi / 3
B = i * j

# TODO: exp(B * theta) => cos(theta) + B * sin(theta)
print repr(exp(B * theta))

