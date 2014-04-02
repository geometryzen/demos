"""
This program uses the bisection method to find the root of f(x)
"""

from math import *
from browser import window

tolerance = 1.0e-6

def f(x):
    return exp(x)*log(x) - x * x

a = window.prompt("Enter first guess", "0")
b = window.prompt("Enter second guess", "1")

dx = abs(b-a)

while dx > tolerance:
    x = (a+b)/2.0
    if (f(a)*f(x)) < 0:
        b = x
    else:
        a = x
    dx = abs(b-a)

print 'Found f(x) = 0 at x = %0.8f +/- %0.8f ' % (x, tolerance)
