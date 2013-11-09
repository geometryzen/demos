'''
Investigating the feasibility of CAS.
'''
from symbolic import *

x = Variable("x")
y = Variable("y")

z = x + x + y

print z
print repr(z)