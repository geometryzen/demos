from e3ga import *
from math import exp, pi

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
I = i * j

print exp(I * pi  / 2)

