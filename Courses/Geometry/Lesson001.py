'''
The first thing we will do is create a linear space.
Our space will have two kinds of elements, one we call vectors, and the other scalars.
With an eye to creating a unified geometric space, the underlying object is a Euclidean.
We use a couple of wrapper functions as a convenience for the user.
We demonstrate that the objects f, g, and k are elements in the space.
'''
class Euclidean:
    def __init__(self, w, x, y):
        if isinstance(w, float):
            self.w = w
        else:
            raise AssertionError("w must be a float")
        self.x = x
        self.y = y
    
    def __str__(self):
        parts = []
        if self.w != 0:
            parts.append(str(self.w))
        if self.x != 0 or self.y != 0:
            parts.append("+".join([str(self.x)+"i", str(self.y)+"j"]))
        return "+".join(parts)
    
    def __repr__(self):
        parts = []
        if self.w != 0:
            parts.append("Scalar(" + str(self.w) + ")")
        if self.x != 0 or self.y != 0:
            parts.append("Vector(" + ", ".join([str(self.x), str(self.y)]) + ")")
        return "+".join(parts)

def Vector(x, y):
    return Euclidean(0, x, y)

def Scalar(w):
    return Euclidean(w, 0, 0)

f = Vector(1, 2)
g = Vector(5, 7)
k = Scalar(4.0)

print "f => " + str(f)
print "g => " + str(g)
print "k => " + str(k)
print "repr(f) => " + repr(f)
print "repr(g) => " + repr(g)
print "repr(k) => " + repr(k)
