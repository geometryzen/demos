'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
There is also a rule for scalar mutiplication.
If f is in V and k is a scalar, then kf is in V.
For al f,g,h in V and c,k scalars, the set also satisfies the following rules:
1. (f + g) + h = f + (g + h)
2. f + g = g + f
3. There exists a neutral element n in V such that f + n = f, for al f in V.
This n is unique and denoted by 0.
'''
class Euclidean:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return Euclidean(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Euclidean(0, self.w * other.x, self.w * other.y, self.w * other.z)
    
    def __eq__(self, other):
        return self.w == other.w and self.x == other.x and self.y == other.y and self.z == other.z
    
    def __str__(self):
        parts = []
        if self.w != 0:
            parts.append(str(self.w))
        if self.x != 0 or self.y != 0 or self.z != 0:
            parts.append("+".join([str(self.x)+"*e1", str(self.y)+"*e2", str(self.z)+"*e3"]))
        return "+".join(parts)
    
    def __repr__(self):
        parts = []
        if self.w != 0:
            parts.append("Scalar(" + str(self.w) + ")")
        if self.x != 0 or self.y != 0 or self.z != 0:
            parts.append("Vector(" + ", ".join([str(self.x), str(self.y), str(self.z)]) + ")")
        if len(parts) > 0:
            return "+".join(parts)
        else:
            return "0"

def Vector(x, y, z):
    return Euclidean(0, x, y, z)

def Scalar(w):
    return Euclidean(w, 0, 0, 0)

f = Vector(1, 2, 3)
g = Vector(3, 5, 7)
h = Vector(11, 13, 17)
k = Scalar(4)
n = Vector(0, 0, 0)

print "f => " + str(f)
print "g => " + str(g)
print "k => " + str(k)
print "n => " + str(n)
print "repr(f) => " + repr(f)
print "repr(g) => " + repr(g)
print "repr(k) => " + repr(k)
print "repr(n) => " + repr(n)


# We want f * g to be in the vector space (a Euclidean vector).
# Python allows us to do this using __mul__.
print "f + g => " + str(f + g)
print str(k) + " * " + str(f) + " => " + str(k * f)

print (f + g) + h == f + (g + h)
print f + g == g + f


print f + n == f
print n != f
print n != n
