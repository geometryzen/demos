'''
The e3ga module pre-defines the standard basis vectors e1, e2 and e3, as well as the pseudoscalar I.
'''
from e3ga import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)
I = e1 * e2 * e3

print e1
print e2
print e3
print I
print e1 ^ e2
print e1 << I
print I * e3
print e3 * I
