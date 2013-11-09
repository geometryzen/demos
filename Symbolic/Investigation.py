'''
Investigating the feasibility of CAS.
'''
from symbolic import *

x = Variable("x")

y = x + x + x

print y
print repr(y)