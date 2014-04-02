"""
This program uses the bisection method to find the root of f(x)
"""

from math import *
from browser import window

tolerance = 1.0e-6

def f(x):
    return exp(x)*log(x) - x * x

a = window.prompt("Enter first guess", "0")
