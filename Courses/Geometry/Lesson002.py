'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
'''
class Euclidean:
    def __init__(self, w, x, y):
        self.w = w
        self.x = x
        self.y = y
    
    def __str__(self):
        parts = []
        if self.w != 0:
            parts.append(str(self.w))
        if self.x != 0 or self.y != 0:
            parts.append("[" + str(self.x) + ", " + str(self.y) + "]")
        return "+".join(parts)
    
    def __repr__(self):
        parts = []
        if self.w != 0:
            parts.append("Scalar(" + str(self.w) + ")")
        if self.x != 0 or self.y != 0:
            parts.append("Vector(" + str(self.x) + ", " + str(self.y) + ")")
        return "+".join(parts)

def Vector(x, y):
    return Euclidean(0, x, y)

def Scalar(w):
    return Euclidean(w, 0, 0)

f = Vector(1, 2)
g = Vector(3, 5)
k = Scalar(4)

print "f => " + str(f)
print "g => " + str(g)
print "k => " + str(k)
print "repr(f) => " + repr(f)
print "repr(g) => " + repr(g)
print "repr(k) => " + repr(k)

# We want f + g to be in the vector space (a Euclidean vector).
# Python allows us to do this using __add__.
print "f : " + repr(f)
print "g : " + repr(g)
print "f + g : " + repr(f + g)
