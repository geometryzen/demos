'''
Under Construction. Nov 3, 2013.
'''
from three import *

distance = 10.0
point = VectorE3(1.0, 2.0, 3.0)

face = Face3(0, 1, 2)

print face
print repr(face)

intersection = Intersection(distance, point, face)

print intersection
print repr(intersection)
