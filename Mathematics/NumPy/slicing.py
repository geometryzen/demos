# slicing.py
from numpy import *
word = array(['H','e','l','p','A'])
print word
'''
print word * 5
'''
print word[4]
print word[0:2]
print word[2:4]
print word[:2] # omitting first index defaults to zero
print word[2:] # omitting second default to len(word)
print word[:]
#print word[1:100]
#rint word[10:0]
print "Watch those minus signs..."
print word[-1] # counting from the right
print word[-2]
print word[-2:]