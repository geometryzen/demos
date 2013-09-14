from e3ga import *
from math import exp, pi

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
I = i * j

# TODO: exp(B * theta) => cos(theta) + B * sin(theta)
print repr(exp(I * pi  / 4))

