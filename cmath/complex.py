from cmath import *

print "----------"
print "construction"
print "----------"
z1 = complex(11.0, 7.0)
print repr(z1)
print "----------"
print "properties"
print "----------"
print z1.real
print z1.imag
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

z2 = complex(5, 3)
one = complex(1, 0)
two = 2
i = complex(0, 1)
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
x = complex(0, 0)
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
x = complex(0, 0)
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
x = complex(1, 0)
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
x = complex(1, 0)
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
print "polar(-1) => " + str(phase(complex(-1.0, 0.0)))
print phase(+1)
print phase(+i)
print phase(-1)
print phase(-i)
print "----------"
print "polar"
print "----------"
print polar(complex(-1.0, 0.0))
print polar(+1)
print polar(+i)
print polar(-1)
print polar(-i)
print "----------"
print "~"
print "----------"
print ~i
#print "----------"
#print "abs"
#print "----------"
#print abs(i)
