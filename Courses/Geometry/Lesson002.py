'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
'''
cclass Euclidean:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
    
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
        if self.x != 0 or self.y != 0:
            parts.append("Vector(" + ", ".join([str(self.x), str(self.y), str(self.z)]) + ")")
        return "+".join(parts)

def Vector(x, y, z):
    return Euclidean(0, x, y, z)

def Scalar(w):
    return Euclidean(w, 0, 0, 0)

f = Vector(1, 2, 3)
g = Vector(3, 5, 7)
k = Scalar(4)

print "f => " + str(f)
print "g => " + str(g)
print "k => " + str(k)
print "repr(f) => " + repr(f)
print "repr(g) => " + repr(g)
print "repr(k) => " + repr(k)


# We want f + g to be in the vector space (a Euclidean vector).
# Python allows us to do this using __add__.
print "f + g => " + str(f + g)
