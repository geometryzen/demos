'''
Investigation into improving accuracy in the use of trigonometric functions.
'''
from math import *

for i in range(-8, 9):
    theta = i * tao / 8
    print cos(theta) * cos(theta) + sin(theta) * sin(theta)
