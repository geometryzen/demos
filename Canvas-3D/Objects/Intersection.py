from three import *

distance = 10.0
point = VectorE3(1.0, 2.0, 3.0)

normal = VectorE3(0.0, 1.0, 0.0)
face = Face3(0, 1, 2, normal)

print face
print repr(face)

intersection = Intersection(distance, point, face)

print intersection
print repr(intersection)
