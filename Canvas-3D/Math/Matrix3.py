'''
Under Construction. Nov 8, 2013
'''
from three import *

m = Matrix3(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)

print "construction"
print Matrix3()
print repr(Matrix3())
print m
print repr(m)
print ""
print "determinant()"
print Matrix3().determinant()
print m.determinant()
print ""
print "transpose()"
print m.transpose()
print m
print m.transpose()
print m

print m.clone()
print m.copy(Matrix3())
print m
m.set(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)
print m

print Matrix3() * 2.0