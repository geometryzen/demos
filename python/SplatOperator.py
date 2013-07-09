# The Python splat operator takes a list as input and expands it into
# positional arguments in a function call.
from eight import *

print repr(Vector3(1,2,3))    # Vector3(1, 2, 3)

print repr(Vector3(*[4,5,6])) # Vector3(4, 5, 6)