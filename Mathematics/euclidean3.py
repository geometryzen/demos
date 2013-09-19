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
assertEqual(a.x, 2)
assertEqual(a.y, 3)
assertEqual(a.z, 4)
assertEqual(a.xy, 5)
assertEqual(a.yz, 6)
assertEqual(a.zx, 7)
assertEqual(a.xyz, 8)

# By default, Euclidean3 is mutable.
assertEqual(True, a.mutable)
a.w = 2
a.x = 3
a.y = 5
a.z = 7
a.xy = 11
a.yz = 13
a.zx = 17
a.xyz = 19
assertEqual(a.w, 2)
assertEqual(a.x, 3)
assertEqual(a.y, 5)
assertEqual(a.z, 7)
assertEqual(a.xy, 11)
assertEqual(a.yz, 13)
assertEqual(a.zx, 17)
assertEqual(a.xyz, 19)

# You can't assign anything other than a number to a coordinate of Euclidean3.
try:
    a.w = "You can't do this"
except TypeError as e:
    assertEqual(str(e),"TypeError: w must be a <type 'float'> or <type 'int'> or <type 'long'> on line 56")
else:
    print "Expecting error when assigning a non-number to a coordinate."
    
# You can chain assignments.
foo = a.w = a.x = 23
assertEqual(foo, 23)
assertEqual(a.w, 23)
assertEqual(a.x, 23)
    
# You can make a Euclidean3 immutable by setting the mutable latch to False.
a.constantify()
assertEqual(False, a.mutable)
try:
    a.w = 1
except AssertionError as e:
    assertEqual(str(e),"AssertionError: Quantity is not mutable on line 71")
else:
    print "Expecting error when assigning to an immutable Euclidean3."

# Most of the time, you will want to construct scalars, vectors or rotors.

# Constructing a scalar, such as an inertial mass, involves only the 'w' component of the Euclidean3. 
mass = Euclidean3(1, 0, 0, 0, 0, 0, 0, 0)
assertEqual(mass.w, 1)
assertEqual(mass.x, 0)
assertEqual(mass.y, 0)
assertEqual(mass.z, 0)
assertEqual(mass.xy, 0)
assertEqual(mass.yz, 0)
assertEqual(mass.zx, 0)
assertEqual(mass.xyz, 0)

print "I hope you enjoyed the tour of Euclidean3!"