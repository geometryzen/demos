# Euclidean3 is the multivector used to represent the Geometric Algebra of 3D Euclidean space.
# It can be found in the e3ga module.
# It is also part of the three module where it unifies and replaces the Vector3 and Quaternion numbers.
# Euclidean3 was designed to be used in conjunction with a graphics library and so was made mutable.
# However, mutability is generally not desirable and so a mutable latch is provided to prevent mutation.
# It should be obvious from the context whether a quantity is expected to be constant.
from three import *

# The following functions are provided for testing purposes.
def assertEqual(actual, expect):
    if expect == actual:
        pass
    else:
        print {"actual": actual, "expect": expect}

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

# Euclidean3 forms a Linear or Vector Space of 2**3=8 dimensions.
a = Euclidean3(1, 2, 3, 4, 5, 6, 7, 8)
assertEqual(a.w, 1)
assertEqual(a.x, 0)
assertEqual(a.y, 0)
assertEqual(a.z, 0)
assertEqual(a.xy, 0)
assertEqual(a.yz, 0)
assertEqual(a.zx, 0)
assertEqual(a.xyz, 0)

# Most of the time, you will want to construct scalars, vectors or rotors.
# Constructing a scalar, like an inertial mass involves only the 'w' component of the Euclidean3. 
mass = Euclidean3(1, 0, 0, 0, 0, 0, 0, 0)
assertEqual(mass.w, 1)
assertEqual(mass.x, 0)
assertEqual(mass.y, 0)
assertEqual(mass.z, 0)
assertEqual(mass.xy, 0)
assertEqual(mass.yz, 0)
assertEqual(mass.zx, 0)
assertEqual(mass.xyz, 0)