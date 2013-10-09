'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
There is also a rule for scalar mutiplication.
If f is in V and k is a scalar, then kf is in V.
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

print "f => " + str(f)
print "g => " + str(g)
print "k => " + str(k)

print "k * f => " + str(k * f)
print "4 * f => " + str(4.0 * f)

scene = CartesianSpace()

def magnitude(v):
    return sqrt(v.x * v.x + v.y * v.y)

def attitude(v):
    a = VectorE3(0, 0, 1)
    b = VectorE3(v.x, v.y, 0) / magnitude(v)
    numer = 1 + b * a
    denom = ScalarE3(sqrt(2 + (a % b)))
    R = numer / denom
    return R

arrowF = ArrowBuilder().scale( magnitude(v1) ).attitude( attitude(v1) ).color("red").build()
scene.add(arrowF)
arrowF.position.set(v1.x / 2.0, v1.y / 2.0, 0.0)

arrowG = ArrowBuilder().scale( magnitude(g) ).attitude( attitude(g) ).color("blue").build()
scene.add(arrowG)
arrowG.position.set(g.x / 2.0 + v1.x, g.y / 2.0 + v1.y, 0.0)

arrowH = ArrowBuilder().scale( magnitude(h) ).attitude( attitude(h) ).color("magenta").build()
scene.add(arrowH)
arrowH.position.set(h.x/2,h.y/2,0)

workbench = Workbench(scene.renderer, scene.camera)

def tick(t):
    scene.render()

def terminate(t):
    done = t > 16
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
