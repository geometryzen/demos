from e3ga import *
from units import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)
I = i * j * k

m = 2 * kilogram
x = (4 * i * 3 * j) * meter

omega = 5  * k / second

print omega

w = I * omega

print w

L = m * (omega)

print L

