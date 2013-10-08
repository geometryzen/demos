'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
There is also a rule for scalar mutiplication.
If f is in V and k is a scalar, then kf is in V.
For al f,g,h in V and c,k scalars, the set also satisfies the following rules:
1. (f + g) + h = f + (g + h)
2. f + g = g + f
'''
class Euclidean:
    def __init__(self, w, x, y):
        if isinstance(w, float):
            self.w = w
        else:
            raise AssertionError("w must be a float")
        if isinstance(x, float):
            self.x = x
        else:
            raise AssertionError("x must be a float")
        if isinstance(y, float):
            self.y = y
        else:
            raise AssertionError("y must be a float")
            
    def __add__(self, other):
        if not isinstance(other, Euclidean):
            raise AssertionError("other must be a Euclidean")
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if not isinstance(other, Euclidean):
            raise AssertionError("other must be a Euclidean")
        return Vector(self.w * other.x, self.w * other.y)

    def __rmul__(self, other):
        if not isinstance(other, float):
            raise AssertionError("other must be a Euclidean or float")
        return Vector(other * self.x, other * self.y)

    def __eq__(self, other):
        if not isinstance(other, Euclidean):
            return False
        return self.w == other.w and self.x == other.x and self.y = other.y
    
    def __str__(self):
        parts = []
        if self.w != 0.0:
            parts.append(str(self.w))
        if self.x != 0.0 or self.y != 0.0:
            parts.append(" + ".join([str(self.x)+" * i", str(self.y)+" * j"]))
        return "+".join(parts)
    
    def __repr__(self):
        parts = []
        if self.w != 0.0:
            parts.append("Scalar(" + str(self.w) + ")")
        if self.x != 0.0 or self.y != 0.0:
            parts.append("Vector(" + ", ".join([str(self.x), str(self.y)]) + ")")
        return "+".join(parts)

def Vector(x, y):
    return Euclidean(0.0, x, y)

def Scalar(w):
    return Euclidean(w, 0.0, 0.0)

f = Vector(1.0, 2.0)
g = Vector(3.0, 5.0)
k = Scalar(4.0)
h = Vector(7.0, 11.0)

print "f => " + str(f)
print "g => " + str(g)
print "k => " + str(k)
print "repr(f) => " + repr(f)
print "repr(g) => " + repr(g)
print "repr(k) => " + repr(k)

print (f + g) + h == f + (g + h)
print f + g == g + f
