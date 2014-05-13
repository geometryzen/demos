from e3ga import *
from random import random

one = ScalarE3(1)
i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)
I = i * j * k

a = random() * i + random() * j + random() * k
b = random() * i + random() * j + random() * k
c = random() * i + random() * j + random() * k

B = b ^ c

print a.dot(b.cross(c))
print a ^ b ^ c
print a.dot(-I * B)
print
print "Triple cross product"
print a.cross(b.cross(c))
print a.dot(c) * b - a.dot(b) * c
print -a << (B)
print
print B << a
print
print -a.dot(B)
print B.dot(a)
print
print a * I
print a.dot(I)
print
print I * a
print I.dot(a)
print
print I * one
print I.dot(one)
print
print one * I
print one.dot(I)
print
print one * one
print one.dot(one)
print
print B * B
print B.dot(B)
