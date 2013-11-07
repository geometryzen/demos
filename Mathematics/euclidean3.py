# Euclidean3 is the multivector used to represent the Geometric Algebra of 3D Euclidean space.
# It can be found in the e3ga module.
# It is also part of the three module where it unifies and replaces the Vector3 and Quaternion numbers.
# Euclidean3 was designed to be used in conjunction with a graphics library and so was made mutable.
# However, mutability is generally not desirable and so a mutable latch is provided to prevent mutation.
# It should be obvious from the context whether a quantity is expected to be constant.
from e3ga import *
from math import exp, cos, sin, sqrt, pi

# The following functions are provided for testing purposes.
def assertEqual(actual, expect):
    if expect == actual:
        pass
    else:
        print {"actual": actual, "expect": expect}

def assertTrue(actual):
    return assertEqual(actual, True)

def assertFalse(actual):
    return assertEqual(actual, False)

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

def isCloseTo(actual, expect):
    epsilon = 1e-10
    error = actual - expect
    quadrance = error % error
    return sqrt(quadrance) < epsilon

print "Euclidean3 forms a Linear or Vector Space of 2**3=8 dimensions."
a = Euclidean3(1, 2, 3, 4, 5, 6, 7, 8)
assertEqual(a.w, 1)
assertEqual(a.x, 2)
assertEqual(a.y, 3)
assertEqual(a.z, 4)
assertEqual(a.xy, 5)
assertEqual(a.yz, 6)
assertEqual(a.zx, 7)
assertEqual(a.xyz, 8)

print "By default, Euclidean3 is mutable."
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

print "You can't assign anything other than a number to a coordinate of Euclidean3."
try:
    a.w = "You can't do this"
except TypeError as e:
    assertEqual(str(e),"TypeError: w must be a <type 'float'> or <type 'int'> or <type 'long'> on line 69")
else:
    print "Expecting error when assigning a non-number to a coordinate."
    
print "You can chain assignments."
foo = a.w = a.x = 23
assertEqual(foo, 23)
assertEqual(a.w, 23)
assertEqual(a.x, 23)
    
print "You can make a Euclidean3 immutable after construction by setting the mutable latch to False."
a.constantify()
assertEqual(False, a.mutable)
print "Testing immutability..."
try:
    a.w = 1
except AssertionError as e:
    print "We got an AssertionError" + repr(e)
    #assertEqual(str(e),"AssertionError: Quantity is not mutable on line 85")
else:
    print "Expecting error when assigning to an immutable Euclidean3."
    
print "You can also make a Euclidean3 immutable upon construction by setting the mutable flag."
zero = Euclidean3(0, 0, 0, 0, 0, 0, 0, 0, False)
assertEqual(False, zero.mutable)

print "Most of the time, you will want to construct scalars, vectors or rotors."

print "Constructing a scalar, such as an inertial mass, involves only the 'w' component of the Euclidean3."
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

print "There is a handy abbreviation for constructing a scalar quantity - ScalarE3(value [,mutable]}"
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

print "You can create scalar constants by setting the mutable flag on construction."
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

print "Constructing a vector, such as a position, involves the x,y,z components of the Euclidean3."
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

print "There is a handy abbreviation for constructing a vector quantity - VectorE3(x, y, z [,mutable]}"
position = VectorE3(2.0, 3.0, 5.0)
assertEqual(position.w, 0)
assertEqual(position.x, 2)
assertEqual(position.y, 3)
assertEqual(position.z, 5)
assertEqual(position.xy, 0)
assertEqual(position.yz, 0)
assertEqual(position.zx, 0)
assertEqual(position.xyz, 0)
assertEqual(True, position.mutable)

print "Lets take a look at the basis vectors for Euclidean3 by setting up some constant unit vectors."
e1 = VectorE3(1.0, 0.0, 0.0, False)
e2 = VectorE3(0.0, 1.0, 0.0, False)
e3 = VectorE3(0.0, 0.0, 1.0, False)
assertEqual(e1.w, 0)
assertEqual(e1.x, 1)
assertEqual(e1.y, 0)
assertEqual(e1.z, 0)
assertEqual(e1.xy, 0)
assertEqual(e1.yz, 0)
assertEqual(e1.zx, 0)
assertEqual(e1.xyz, 0)
assertEqual(False, e1.mutable)

print "Euclidean3 adopts standard notation for basis vectors - e1,e2,e3."
assertEqual("e1", str(e1))
assertEqual("e2", str(e2))
assertEqual("e3", str(e3))
assertEqual("3*e1+4*e2+12*e3", str(VectorE3(3.0, 4.0, 12.0)))

assertEqual(VectorE3(3, 4, 12).magnitude(), 13)

print "The scalar product is available using the Python % operator."
print "Between vectors this is referred to as the dot product."
print "Here are the orthonormal conditions satisfied by our basis vectors."
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

# Let's prepare the other basis bivectors.
e23 = (e2 ^ e3).constantify()
assertEqual(e23.w, 0)
assertEqual(e23.x, 0)
assertEqual(e23.y, 0)
assertEqual(e23.z, 0)
assertEqual(e23.xy, 0)
assertEqual(e23.yz, 1)
assertEqual(e23.zx, 0)
assertEqual(e23.xyz, 0)
assertEqual(False, e23.mutable)
e31 = (e3 ^ e1).constantify()

assertEqual("e12", str(e12))
# We can create the same bivector directly from it's components.
assertEqual(e12, Euclidean3(0, 0, 0, 0, 1, 0, 0, 0))
# Again, there is a shorter and more descriptive constructor function.
assertEqual(e12, BivectorE3(1, 0, 0))
assertEqual(repr(e12), "BivectorE3(1, 0, 0)")

# e12 squares to -1, but notice that the result is a Euclidean3 (ScalarE3), not a float.
assertEqual(e12 * e12, ScalarE3(-1.0))
assertEqual(e12 * e12, ScalarE3(-1))
assertTrue(e12 * e12 == ScalarE3(-1.0))
assertTrue(e12 * e12 == ScalarE3(-1))
assertFalse(e12 * e12 == -1.0)
assertFalse(e12 * e12 == -1)

print "Bivectors, like e12, that square to -1 are the generators of rotations."
# A rotor can be constructed from a normalized bivector using the exponential function.
# Notice how a rotation through theta is expressed as a half-angle in the rotor, R
theta = pi / 2
R = exp(-e12 * theta / 2)
assertEqual(R.w, cos(theta / 2))
assertEqual(R.x, 0)
assertEqual(R.y, 0)
assertEqual(R.z, 0)
assertEqual(R.xy, -sin(theta / 2))
assertEqual(R.yz, 0)
assertEqual(R.zx, 0)
assertEqual(R.xyz, 0)
assertEqual(True, R.mutable)
R.constantify()
assertEqual(False, R.mutable)

print "The reversion of a multivector is the multivector obtained by reversing the vectors."
print "We use the Python ~ unary operator to perform reversion." 
A = Euclidean3(1, 2, 3, 4, 5, 6, 7, 8)
revA = ~A
print "Under reversion, the signs of the components (by grade) follow a ++--++--... pattern."
assertEqual(revA.w, A.w)
assertEqual(revA.x, A.x)
assertEqual(revA.y, A.y)
assertEqual(revA.z, A.z)
assertEqual(revA.xy, -A.xy)
assertEqual(revA.yz, -A.yz)
assertEqual(revA.zx, -A.zx)
assertEqual(revA.xyz, -A.xyz)

print "Rotors do their job of rotation by being applied on either side of their multivector operand."
print "R has been generated by a bivector that rotates from e1 to e2, a counter-clockwise rotation in the xy-plane."
print "The angle, theta, was pi / 2, and the half-angle used in generating R was theta / 2, or pi / 4."
print "So we expect R to produce a rotation of theta = pi /2 in the xy-plane."
assertTrue(isCloseTo(R * e1 * ~R, e2))
assertTrue(isCloseTo(e1, e1))
assertFalse(isCloseTo(e1, e2))

# Rotors can be thought of as geometric angles because they contain all the information for the rotation -
# the magnitude, the aspect and the orientation.

print "Finally, we come to the Pseudoscalar, geometrically interpreted as an oriented and weighted volume element."
I = e1 ^ e2 ^ e3
# Here are some other ways of constructing the pseudoscalar.
assertEqual(Euclidean3(0,0,0,0,0,0,0,1), I)
assertEqual(PseudoscalarE3(1), I)
assertEqual(e1 * e2 * e3, I)

print "The pseudoscalar has lots of interesting properties, some of which depend upon the dimensionality of the linear space."
# I squares to -1
assertEqual(I * I, ScalarE3(-1))
# It commutes with other elements.
assertEqual(I * one, one * I)
assertEqual(I * e1, e1 * I)
assertEqual(I * e12, e12 * I)
# It can be use to compute the Hodge dual.
assertEqual(one * I, I)
assertEqual(e1 * I, e23)
assertEqual(e2 * I, e31)
assertEqual(e3 * I, e12)
assertEqual(e12 * I, -e3)
assertEqual(e23 * I, -e1)
assertEqual(e31 * I, -e2)
assertEqual(I * I, -one)

# We've been assuming the geometric product all along using the standard Python operator for multiplication.
# Between vectors we have the following identity.
a = VectorE3(2,3,5)
b = VectorE3(7,11,13)
assertEqual(a * b, (a % b) + (a ^ b))
# Notice the need for parenthesis because of Python precedence rules.
assertEqual(a * b, a % b + (a ^ b))
# This is what Python does without the parenthesis.
assertEqual(((a % b) + a) ^ b, a % b + a ^ b)

print "There's also the left- and right-contraction which are represented by the Python bitshift operators << and >>."
assertEqual(one << e12, e12)
assertEqual(e1 << e12, e2)
assertEqual(e2 << e12, -e1)
assertEqual(e3 << e12, zero)


print "I hope you enjoyed the tour of Euclidean3!"