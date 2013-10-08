from browser import WindowAnimationRunner
from geometry import CartesianSpace, ArrowBuilder
from workbench import Workbench
from e3ga import *
from math import exp, sqrt, pi

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

f = Vector(0.0, 4.0)
g = Vector(-3.0, 1.0)
h = f + g
print "f => " + str(f)
print "g => " + str(g)
print "f + g => " + str(h)

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

arrowF = ArrowBuilder().name("f").scale( magnitude(f) ).attitude( attitude(f) ).color(0xFF0000).build()#.axis(f.x, f.y, 0).build()
scene.add(arrowF)
arrowF.position.set(f.x/2,f.y/2,0)

arrowG = ArrowBuilder().name("g").scale( magnitude(g) ).attitude( attitude(g) ).color(0x0000FF).build()#.axis(f.x, f.y, 0).build()
scene.add(arrowG)
arrowG.position.set(g.x/2,g.y/2,0)

arrowH = ArrowBuilder().name("h").scale( magnitude(h) ).attitude( attitude(h) ).color("magenta").build()#.axis(f.x, f.y, 0).build()
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

