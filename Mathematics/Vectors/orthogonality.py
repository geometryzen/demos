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

print "A = %s" % A
print "B = %s" % B

print "C.dot(A) = %s" % C.dot(A)
print "C.dot(B) = %s" % C.dot(B)
print "C.dot(C) = %s" % C.dot(C)

