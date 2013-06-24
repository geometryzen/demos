# Vector3 demonstration
from three import *
#
# It is important to realize that Vector3 is mutable.
# This contrasts to the usual approach of treating mathematical
# objects as immutable types.

a = Vector3(1,1,1)
print str(a)
print repr(a)
print str(type(a))
print repr(type(a))
a.x = 2
a.y = 3
a.z = 5
print a
a.x = 0
a.y = 0
a.z = 0
