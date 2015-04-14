'''
The e2ga module pre-defines the standard basis vectors e1 and e2, as well as the pseudoscalar I.
'''
from e2ga import *

#e1 = VectorE2(1,0)
e2 = VectorE2(0,1)
I = e1 * e2

print e1
print e2
print e1 * e2
print e2 << I
