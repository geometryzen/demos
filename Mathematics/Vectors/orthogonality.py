'''
Calculate the cross product of the vectors A, B,
and verify that it is perpendicular to both A and B.
'''
from e3ga import *
from units import *

A = VectorE3(2,3,0) * meter
B = VectorE3(-1,1,4) * meter

print "A = %s" % A
print "B = %s" % B
print
C = A.cross(B)
print "C = A x B = %s" % C
print
print "Verify that A and B were not changed."
print "A = %s" % A
print "B = %s" % B
print
print "C.dot(A) = %s" % C.dot(A)
print "C.dot(B) = %s" % C.dot(B)
print "C.dot(C) = %s" % C.dot(C)
print
print "The contraction is the same as the dot product (for vectors)."
print
print "C >> A = %s" % (C >> A)
print "C >> B = %s" % (C >> B)
print "C >> C = %s" % (C >> C)
print
print "C >> A = %s" % (C << A)
print "C >> B = %s" % (C << B)
print "C >> C = %s" % (C << C)
