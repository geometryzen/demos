# Vector3 demonstration
from three import *

a = Vector3(1,1,1)

print str(a)
print repr(a)
print str(type(a))
print repr(type(a))

#
# It is important to realize that Vector3 is mutable.
# This contrasts to the usual approach of treating mathematical
# objects as immutable types.
a.x = 2
a.y = 3
a.z = 5
print a

# The string value of the zero vector is just "0"
print str(Vector3(0,0,0))
print repr(Vector3(0,0,0))
