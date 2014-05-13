from e3ga import *
from units import *
from math import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)
I = i * j * k

m = 2 * kilogram
x = (4 * i + 3 * k) * meter
print x

omega = 7  * k / second

print omega

w = I * omega

print w

L = m * (x * x * omega - omega.dot(x) * x)

print L

v = omega.cross(x)

print v

print L.dot(x)
print L.dot(v)

L = m * (x * x * w - x * (w ^ x))

print L

u = x / magnitude(x)

