from e3ga import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)

print i.dot(j.cross(k))
print i ^ j ^ k