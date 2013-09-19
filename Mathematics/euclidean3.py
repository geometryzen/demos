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
    
# You can make a Euclidean3 immutable after construction by setting the mutable latch to False.
a.constantify()
assertEqual(False, a.mutable)
try:
    a.w = 1
except AssertionError as e:
    assertEqual(str(e),"AssertionError: Quantity is not mutable on line 72")
else:
    print "Expecting error when assigning to an immutable Euclidean3."
    
# You can also make a Euclidean3 immutable upon construction by setting the mutable flag.
zero = Euclidean3(0, 0, 0, 0, 0, 0, 0, 0, False)
assertEqual(False, zero.mutable)

# Most of the time, you will want to construct scalars, vectors or rotors.

# Constructing a scalar, such as an inertial mass, involves only the 'w' component of the Euclidean3. 
mass = Euclidean3(19, 0, 0, 0, 0, 0, 0, 0)
assertEqual(mass.w, 19)
assertEqual(mass.x, 0)
assertEqual(mass.y, 0)
assertEqual(mass.z, 0)
assertEqual(mass.xy, 0)
assertEqual(mass.yz, 0)
assertEqual(mass.zx, 0)
assertEqual(mass.xyz, 0)
assertEqual(True, mass.mutable)

# There is a handy abbreviation for constructing a scalar quantity - ScalarE3(value [,mutable]}
mass = ScalarE3(23)
assertEqual(mass.w, 23)
assertEqual(mass.x, 0)
assertEqual(mass.y, 0)
assertEqual(mass.z, 0)
assertEqual(mass.xy, 0)
assertEqual(mass.yz, 0)
assertEqual(mass.zx, 0)
assertEqual(mass.xyz, 0)
assertEqual(True, mass.mutable)

# You can create scalar constants by setting the mutable flag on construction.
one = ScalarE3(1, False)
assertEqual(one.w, 1)
assertEqual(one.x, 0)
assertEqual(one.y, 0)
assertEqual(one.z, 0)
assertEqual(one.xy, 0)
assertEqual(one.yz, 0)
assertEqual(one.zx, 0)
assertEqual(one.xyz, 0)
assertEqual(False, one.mutable)

# Constructing a vector, such as a position, involves the x,y,z components of the Euclidean3.
position = Euclidean3(0, 2, 3, 5, 0, 0, 0, 0)
assertEqual(position.w, 0)
assertEqual(position.x, 2)
assertEqual(position.y, 3)
assertEqual(position.z, 5)
assertEqual(position.xy, 0)
assertEqual(position.yz, 0)
assertEqual(position.zx, 0)
assertEqual(position.xyz, 0)
assertEqual(True, position.mutable)

# There is a handy abbreviation for constructing a vector quantity - VectorE3(x, y, z [,mutable]}
position = VectorE3(2, 3, 5)
assertEqual(position.w, 0)
assertEqual(position.x, 2)
assertEqual(position.y, 3)
assertEqual(position.z, 5)
assertEqual(position.xy, 0)
assertEqual(position.yz, 0)
assertEqual(position.zx, 0)
assertEqual(position.xyz, 0)
assertEqual(True, position.mutable)

# Lets take a look at the basis vectors for Euclidean3 by setting up some constant unit vectors.
e1 = VectorE3(1, 0, 0, False)
e2 = VectorE3(0, 1, 0, False)
e3 = VectorE3(0, 0, 1, False)
assertEqual(e1.w, 0)
assertEqual(e1.x, 1)
assertEqual(e1.y, 0)
assertEqual(e1.z, 0)
assertEqual(e1.xy, 0)
assertEqual(e1.yz, 0)
assertEqual(e1.zx, 0)
assertEqual(e1.xyz, 0)
assertEqual(False, e1.mutable)

# Euclidean3 adopts Hamilton's notation for basis vectors - i,j,k.
assertEqual("i", str(e1))
assertEqual("j", str(e2))
assertEqual("k", str(e3))
assertEqual("3*i+4*j+12*k", str(VectorE3(3, 4, 12)))

# TODO: Not sure whether to use length or something else.
assertEqual(13, len(VectorE3(3, 4, 12)))

# The scalar product is available using the Python % operator.
# Between vectors this is referred to as the dot product.
# Here are the orthonormal conditions satisfied by our basis vectors.
assertEqual(1, e1 % e1)
assertEqual(1, e2 % e2)
assertEqual(1, e3 % e3)
assertEqual(0, e1 % e2)
assertEqual(0, e2 % e3)
assertEqual(0, e3 % e1)

# Here is the scalar product being used for projection.
assertEqual(3,  e1 % VectorE3(3, 4, 12))
assertEqual(4,  e2 % VectorE3(3, 4, 12))
assertEqual(12, e3 % VectorE3(3, 4, 12))

# Things get a bit more interesting when we extend the vectors using the outer product.
e12 = e1 ^ e2
assertEqual(e12.w, 0)
assertEqual(e12.x, 0)
assertEqual(e12.y, 0)
assertEqual(e12.z, 0)
assertEqual(e12.xy, 1)
assertEqual(e12.yz, 0)
assertEqual(e12.zx, 0)
assertEqual(e12.xyz, 0)
assertEqual(True, e12.mutable)
e12.constantify()
assertEqual(False, e12.mutable)

assertEqual("ij", str(e12))
assertEqual(e12, BivectorE3(1, 0, 0))
assertEqual(repr(e12), "BivectorE3(1, 0, 0)")

# Pure bivectors, like e12, that square to -1 are the generators of rotations.
assertEqual(e12 * e12, ScalarE3(-1))
assertEqual(e12 * e12 == ScalarE3(-1), True)
assertEqual(e12 * e12 == -1, False)

print "I hope you enjoyed the tour of Euclidean3!"