'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
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
    
    def __str__(self):
        parts = []
        if self.w != 0.0:
            parts.append(str(self.w))
        if self.x != 0.0 or self.y != 0.0:
            parts.append("+".join([str(self.x)+"i", str(self.y)+"j"]))
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
g = Vector(5.0, 7.0)
k = Scalar(4.0)
print "f => " + str(f)
print "g => " + str(g)
print "k => " + str(k)
print "repr(f) => " + repr(f)
print "repr(g) => " + repr(g)
print "repr(k) => " + repr(k)


# We want f + g to be in the vector space (a Euclidean vector).
# Python allows us to do this using __add__.
print "f + g => " + str(f + g)
