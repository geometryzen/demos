# The complex number algebra is isomorphic to the even sub-algebra of the Euclidean Plane.
# This program demonstrates this fact.
from cmath import *
from e2ga import *

useComplex = False

def constructor(x, y):
    if useComplex:
        return complex(x,y)
    else:
        return Euclidean2(x, 0, 0, y)
    
def Re(z):
    if useComplex:
        return z.real
    else:
        return z.w

def Im(z):
    if useComplex:
        return z.imag
    else:
        return z.xy
    
def computePhase(z):
    if useComplex:
        return phase(z);
    else:
        return phase(complex(z.w,z.xy))

def computePolar(z):
    if useComplex:
        return polar(z);
    else:
        return polar(complex(z.w,z.xy))

print "----------"
print "construction"
print "----------"
z1 = constructor(11.0, 7.0)
print repr(z1)
print "----------"
print "properties"
print "----------"
print Re(z1)
print Im(z1)
print "----------"
print "representations"
print "----------"
print z1
print str(z1)
print "----------"
print "type"
print "----------"
print type(z1)
print str(type(z1))
print repr(type(z1))

z2 = constructor(5, 3)
one = constructor(1, 0)
two = constructor(2, 0)
i = constructor(0, 1)
zs = [one, two, i, z1, z2]
print "----------"
print "Addition (+)"
print "----------"
for a in zs:
    for b in zs:
        print str(a) + " + " + str(b) + " => " + str(a+b)
print "----------"
print "+="
print "----------"
x = constructor(0, 0)
print x
x += 1
print x
x += z1
print x
print "----------"
print "Subtraction (-)"
print "----------"
for a in zs:
    for b in zs:
        print str(a) + " - " + str(b) + " => " + str(a-b)
print "----------"
print "-="
print "----------"
x = constructor(0, 0)
print x
x -= 1
print x
x -= z1
print x
print "----------"
print "Multiplication (*)"
print "----------"
for a in zs:
    for b in zs:
        print str(a) + " * " + str(b) + " => " + str(a*b)
print "----------"
print "*="
print "----------"
x = constructor(1, 0)
print x
x *= 1
print x
x *= z1
print x
x *= z2
print x

print "----------"
print "Division (/)"
print "----------"
for a in zs:
    for b in zs:
        print str(a) + " / " + str(b) + " => " + str(a/b)
print "----------"
print "*="
print "----------"
x = constructor(1, 0)
print x
x /= 1
print x
x /= z1
print x

print "----------"
print "Equality"
print "----------"
print z1 == z1
print z1 != z1
print z1 == z2
print z1 != z2
print "----------"
print "phase"
print "----------"
print "phase(complex(-1,0)) => " + str(computePhase(constructor(-1.0, 0.0)))
print computePhase(+one)
print computePhase(+i)
print computePhase(-one)
print computePhase(-i)
print "----------"
print "polar"
print "----------"
print "polar(complex(-1,0)) => " + str(computePolar(constructor(-1.0, 0.0)))
print computePolar(+one)
print computePolar(+i)
print computePolar(-one)
print computePolar(-i)
print "----------"
print "~"
print "----------"
print ~i
#print "----------"
#print "abs"
#print "----------"
#print abs(i)
