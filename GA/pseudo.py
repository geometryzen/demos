from e3ga import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)
I = i * j * k

a = 5 * i + 3 * j + 2 * k

print a.dot(j.cross(k))
print a ^ j ^ k
print a.dot(-I * (j^k))