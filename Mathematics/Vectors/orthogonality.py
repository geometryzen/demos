'''
Calculate the cross product of the vectors A, B,
and verify that it is perpendicular to both A and B.
'''
from e3ga import *

A = VectorE3(2,3,0)
B = VectorE3(-1,1,4)

print "A = %s" % A
print "B = %s" % B

C = A.cross(B)

print "C = A x B = %s" % C
