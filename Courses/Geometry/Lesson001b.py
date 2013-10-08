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
            
    def quadrance(self):
        x = self.x
        y = self.y
        return x * x + y * y
    
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

f = Vector(0.0, 2.0)
g = Vector(5.0, 7.0)
k = Scalar(4.0)

scene = CartesianSpace()

def attitude(v):
    a = VectorE3(0, 0, 1)
    b = VectorE3(v.x, v.y, 0) / v.magnitude()
    numer = 1 + b * a
    print numer
    denom = ScalarE3(sqrt(2 + (a % b)))
    R = numer / denom
    print R
    return R

# TODO: Need axis function for the ArrowBuilder (attitude is too advanced). Or maybe coordinates?
magnitude = sqrt( f.quadrance() )
arrowF = ArrowBuilder().name("f").scale(magnitude).attitude( attitude(f) ).color(0xFFFF00).build()#.axis(f.x, f.y, 0).build()
scene.add(arrowF)

workbench = Workbench(scene.renderer, scene.camera)

def tick(t):
    scene.render()

def terminate(t):
    done = t > 4
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
